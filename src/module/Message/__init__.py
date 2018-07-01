from .content_type import determine_content_type


class Message:
    def __init__(self, content):
        self.content = content
        self.type = determine_content_type(content)

    # Todo: Logging, censoring
