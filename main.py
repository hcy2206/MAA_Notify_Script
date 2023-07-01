from pypushdeer import PushDeer
import re

# LOG_PATH = 'D:\Green Tools\MAA-Arknights\debug\gui.log' # 日志文件路径
LOG_PATH = 'gui.log'  # 测试用 日志文件路径
KEYWORD_START = 'Main windows log clear.'
KEYWORD_ERROR = '任务出错'
KEYWORD_WARNING = '代理指挥失误'
KEYWORD_REPORT = ['开始任务: Fight', '完成任务: Fight', '掉落统计:']
KEYWORD_REPORT_BREAK = ['已开始行动', '代理指挥失误']

PUSHDEER_SERVER = 'http://8.130.41.75:8800'  # PushDeer 服务器地址
PUSHDEER_KEY = 'PDU1TsCU2jU7jdh8LzZIJUjs9wf5nqR8coLlo'  # PushDeer API Key


def search_keyword():
    with open(LOG_PATH, 'r', encoding='utf-8') as f:
        lines = f.readlines()
        start_line = 0
        line_error = ''
        line_report = []
        line_report_count = [0, 0]
        for i in range(len(lines)):  # 找到最后一个开始标志 KEYWORD_START
            if KEYWORD_START in lines[i]:
                start_line = i
        for i in range(start_line, len(lines)):  # 从最后一个开始标志 KEYWORD_START 开始往后找
            if KEYWORD_ERROR in lines[i] or KEYWORD_WARNING in lines[i]:
                line_error += lines[i] + '\n'
            if KEYWORD_REPORT[0] in lines[i]:  # 记录 开始任务: Fight 的行数
                line_report_count[0] = i
            if KEYWORD_REPORT[1] in lines[i]:  # 记录 完成任务: Fight 的行数
                line_report_count[1] = i
        if line_report_count[0] == 0 or line_report_count[1] == 0:
            line_report = ['No Fight.']
        for i in range(line_report_count[1], line_report_count[0], -1):  # 倒序查找，找到最后一个 掉落统计: 的行数
            if line_report_count[1] - line_report_count[0] == 1:
                line_report = ['No Drop.']
                break
            if KEYWORD_REPORT[2] in lines[i]:
                for j in range(i, line_report_count[1]):
                    # 跳过 代理指挥失误
                    if KEYWORD_REPORT_BREAK[0] in lines[j] or KEYWORD_REPORT_BREAK[1] in lines[j]:
                        break
                    line_report.append(re.sub(r'\s*\(.*?\)', '', lines[j]))  # 去除掉落统计行中的括号及括号内内容
                break
        if KEYWORD_ERROR in line_error or KEYWORD_WARNING in line_error:
            return line_error, line_report
        else:
            return 'No Error Log.', line_report


def line_report_format(line_report):
    if len(line_report) == 1:
        return line_report[0]
    for i in range(len(line_report)):
        line_report[i] = re.sub(r'\n', '', line_report[i])
        if i == 0:
            line_report[i] = re.sub(r'<.*><>', '', line_report[i])
    # 将 line_report 从第 1 行开始(跳过第 0 行) 按照':'分割为两列，储存为二维数组
    line_report_array = [i.split(':') for i in line_report[1:]]
    # # 将二维数组转换为 markdown 表格格式
    # line_report_md = '| 材料 | 数量 |' + '\n' + '|:---:|:---:|\n'
    # for i in range(len(line_report_array)):
    #     line_report_md += '| ' + ' | '.join(line_report_array[i]) + ' |\n'
    # line_report_md = line_report[0] + '\n\n' + line_report_md
    line_report_output = line_report[0] + '\n\n'
    for i in range(len(line_report_array)):
        line_report_output += line_report_array[i][0] + '    ' + line_report_array[i][1] + '\n\n'
    return line_report_output


def notify(text, desc):
    pushdeer = PushDeer(PUSHDEER_SERVER, PUSHDEER_KEY)
    pushdeer.send_markdown(text, desc)


if __name__ == '__main__':
    log, line_report = search_keyword()
    # print(line_report)
    if KEYWORD_ERROR in log:
        text = '## ⚠️MAA has finished your job, but something failed!'
        desc = "### *Here's the ERROR log*:\n\n" + log + '\n\n' + \
               "### *Here's the drop report*:\n\n" + line_report_format(line_report)
        # notify('## ⚠️MAA has finished your job, but something failed!', "### *Here's the ERROR log*:\n\n" + log)
    elif KEYWORD_WARNING in log:
        text = '## ⚠️MAA has finished your job, but there\'s warning!'
        desc = "### *Here's the WARNING log*:\n\n" + log + '\n\n' + \
               "### *Here's the drop report*:\n\n" + line_report_format(line_report)
        # notify('## ⚠️MAA has finished your job, but there\'s warning!', "### *Here's the WARNING log*:\n\n" + log)
    else:
        text = '## 🎉MAA has finished your job, and everything is perfect!'
        desc = "### *Here's the drop report*:\n\n" + line_report_format(line_report)
        # notify('## 🎉MAA has finished your job, and everything is perfect!', '*' + log + '*')
    notify(text, desc)
