def create_single_text_message(message):
    if message == 'ありがとう':
        message = 'どういたしまして！'
    elif message == 'なにしてる？':
        message = 'YouTubeみてる'
    test_message = [
        {
            'type': 'text',
            'text': message
        }
    ]
    return test_message
