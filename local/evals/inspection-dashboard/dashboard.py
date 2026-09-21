def summarize(readings):
    status = 'clear'
    message = 'All sensors clear'
    for name, reading in readings:
        if reading == 'fault':
            status = 'fault'
            message = f'Fault at {name}'
        elif reading is None:
            status = 'unknown'
        elif reading == 'clear':
            message = 'All sensors clear'
    return {'status': status, 'message': message}
