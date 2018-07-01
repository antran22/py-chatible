from mongodb import mongo
from api.send_message import send_message


def pair(user):
    partner_record = mongo.db.queue.find_one_and_delete({})
    if partner_record is None:
        user.enqueue()
    else:
        partner_id = partner_record["user_id"]
        partner = User(partner_id)
        user.partner = partner_id
        user.status = "paired"

        partner.partner = user.user_id
        partner.status = "paired"
        send_message(user.user_id, "Paired")
        send_message(partner.user_id, "Paired")


def unpair(user):
    user.pull_info()
    partner = User(user.partner)

    user.partner = None
    user.status = "inactive"

    partner.partner = None
    partner.status = "inactive"

    send_message(user.user_id, "Unpaired")
    send_message(partner.user_id, "Unpaired")


class User:
    def __init__(self, user_id):
        self.user_id = int(user_id)
        self.__fullname = None
        self.__gender = None
        self.__avatar = None
        self.__status = None
        self.__partner = None

    def enqueue(self):
        mongo.db.queue.insert_one({
            "user_id": self.user_id
        })
        mongo.db.user.update_one({
            "user_id": self.user_id
        }, {
            "$set": {
                "status": "pending"
            }
        })

    def register(self, fullname, gender, avatar):
        self.__fullname = fullname,
        self.__gender = gender
        self.__avatar = avatar
        mongo.db.user.insert_one(
            {
                "user_id": self.user_id,
                "gender": gender,
                "fullname": fullname,
                "avatar": avatar,
                "status": "inactive",
                "partner": None
            }
        )

    def pull_info(self):
        user_record = mongo.db.user.find_one(
            {
                "user_id": self.user_id
            }
        )
        self.__fullname = user_record["fullname"]
        self.__gender = user_record["gender"]
        self.__avatar = user_record["avatar"]
        self.__status = user_record["status"]
        self.__partner = user_record["partner"]

    # Todo: Shorten these
    @property
    def fullname(self):
        if self.__fullname is None:
            self.pull_info()
        return self.__fullname

    @property
    def gender(self):
        if self.__gender is None:
            self.pull_info()
        return self.__gender

    @property
    def avatar(self):
        if self.__avatar is None:
            self.pull_info()
        return self.__avatar

    @property
    def status(self):
        if self.__status is None:
            self.pull_info()
        return self.__status

    @status.setter
    def status(self, new_status):
        self.__status = new_status
        mongo.db.user.update_one(
            {
                "user_id": self.user_id
            }, {
                "$set": {
                    "status": new_status
                }
            }
        )

    @property
    def partner(self):
        if self.__status is None:
            self.pull_info()
        return self.__partner

    @partner.setter
    def partner(self, partner_id):
        self.__partner = partner_id
        mongo.db.user.update_one(
            {
                "user_id": self.user_id
            }, {
                "$set": {
                    "partner": partner_id
                }
            }
        )
