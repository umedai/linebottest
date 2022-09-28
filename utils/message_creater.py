def create_single_text_message(message):
    if message == 'ありがとう':
        message = 'どういたしまして！'
    elif message == 'なにしてる？':
        message = 'YouTubeみてる'
    elif message == '予約できる日を教えてください':
        message = '７に予約ができます'
    test_message = [
        {
            'type': 'text',
            'text': message
        }
    ]
    return test_message
