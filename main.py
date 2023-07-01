from pypushdeer import PushDeer

LOG_PATH = 'D:\Green Tools\MAA-Arknights\debug\gui.log'
KEYWORD_START = 'Main windows log clear.'
KEYWORD_ERROR = '任务出错'
KEYWORD_WARNING = '代理指挥失误'

PUSHDEER_SERVER = 'http://8.130.41.75:8800'
PUSHDEER_KEY = 'PDU1TsCU2jU7jdh8LzZIJUjs9wf5nqR8coLlo'


def search_keyword():
    with open(LOG_PATH, 'r', encoding='utf-8') as f:
        lines = f.readlines()
        start_line = 0
        line_error = ''
        for i in range(len(lines)):
            if KEYWORD_START in lines[i]:
                start_line = i
        for i in range(start_line, len(lines)):
            if KEYWORD_ERROR in lines[i] or KEYWORD_WARNING in lines[i]:
                line_error += lines[i] + '\n'
        if KEYWORD_ERROR in line_error or KEYWORD_WARNING in line_error:
            return line_error
        else:
            return 'No Error Log.'


def notify(text, desc):
    pushdeer = PushDeer(PUSHDEER_SERVER, PUSHDEER_KEY)
    pushdeer.send_markdown(text, desc)


if __name__ == '__main__':
    log = search_keyword()
    if KEYWORD_ERROR in log:
        notify('## ⚠️MAA has finished your job, but something failed!', "### *Here's the ERROR log*:\n\n" + log)
    elif KEYWORD_WARNING in log:
        notify('## ⚠️MAA has finished your job, but there\'s warning!', "### *Here's the WARNING log*:\n\n" + log)
    else:
        notify('## 🎉MAA has finished your job, and everything is perfect!', '*' + log + '*')