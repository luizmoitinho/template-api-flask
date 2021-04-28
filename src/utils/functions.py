


def create_message_response(status, message, name_content, content):
    response =  {

    }

    response['status'] = status
    response['message'] = message
    if(name_content and content):
        response[name_content] = content

    return response
