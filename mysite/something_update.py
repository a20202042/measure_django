from django.shortcuts import render
from mysite import models, forms
from django.shortcuts import redirect
from django.http import HttpResponse, HttpResponseRedirect, JsonResponse
from django.template.loader import render_to_string
import base64, os, json, statistics, numpy
from django.shortcuts import get_object_or_404


def cpk_check(ca, cp, cpk):
    if abs(ca) <= float(0.125):
        ca_ = ['A+', '製程穩定']
    elif abs(ca) > float(0.125) and abs(ca) <= float(0.25):
        ca_ = ['A', '製程穩定']
    elif abs(ca) > float(0.25) and abs(ca) <= float(0.5):
        ca_ = ['B', '製程能力降低']
    elif abs(ca) > float(0.5):
        ca_ = ['C', '製程警報']

    if abs(cp) >= 1.67:
        cp_ = ['A+', '製程穩定']
    elif abs(cp) >= 1.33 and abs(cp) < 1.67:
        cp_ = ['A', '製程穩定']
    elif abs(cp) >= 1.0 and abs(cp) < 1.33:
        cp_ = ['B', '製程能力降低']
    elif abs(cp) >= 0.67 and abs(cp) < 1.0:
        cp_ = ['C', '製程警報']
    elif abs(cp) < 0.67:
        cp_ = ['D', '製程警報']

    if abs(cpk) >= 1.67:
        cpk_ = ['A+', '製程穩定']
    elif abs(cpk) >= 1.33 and abs(cpk) < 1.67:
        cpk_ = ['A', '製程穩定']
    elif abs(cpk) >= 1.0 and abs(cpk) < 1.33:
        cpk_ = ['B', '製程能力降低']
    elif abs(cpk) >= 0.67 and abs(cpk) < 1.0:
        cpk_ = ['C', '製程警報']
    elif abs(cpk) < 0.67:
        cpk_ = ['D', '製程警報']
    return ca_, cp_, cpk_


def update_something():
    latest_measure_work_order_id = models.measure_values.objects.latest('id').measure_work_order.id
    time = models.measure_values.objects.latest('id').time_now
    # print(latest_measure_work_order_id, time)
    # id = latest_measure_work_order_id
    id = 242
    project_id = models.measurement_work_order.objects.get(id=id).project_measure_id
    project = models.project.objects.get(id=project_id)
    project_image = models.project.objects.get(id=project_id).project_image
    project_name = models.project.objects.get(id=project_id).project_name
    w = models.measurement_work_order.objects.get(id=id)
    work_order_measure_items = models.work_order_measure_items.objects.filter(measurement_work_order_id=id).all()
    measure_values = models.measure_values.objects.filter(measure_work_order_id=id).all()
    measure_values_data = []
    number_of_parts = w.number_of_parts
    part_remake = models.work_order_parts_reamke.objects.filter(work_order_id=id)
    work_order_appearance = models.work_order_appearance_defect.objects.filter(work_order_id=id)
    measure_item_data = models.work_order_measure_items.objects.filter(measurement_work_order_id=id).values(
        'measurement_items', 'id')
    cpk_data = []
    for item in measure_item_data:
        # print(item['measurement_items'])
        # print(item['id'])
        specification_center = models.work_order_measure_items.objects.get(id=item['id']).specification_center
        upper_limit = models.work_order_measure_items.objects.get(id=item['id']).upper_limit
        lower_limit = models.work_order_measure_items.objects.get(id=item['id']).lower_limit
        t = float()
        t = upper_limit - lower_limit
        all_value = models.measure_values.objects.filter(measure_work_order_measure_item_id=item['id']).values(
            'measure_value')
        measure_count = models.work_order_measure_items.objects.get(id=item['id']).measure_number
        number = 0
        data = []
        measure_all_data = []
        average_data = []
        # print(measure_count)
        for i in all_value:
            number = number + 1
            data.append(float(i['measure_value']))
            # print(data)
            if int(measure_count) == number:
                number = 0
                measure_all_data.append(data)
                data = []
        for i in measure_all_data:
            average_data.append(round(statistics.mean(i), 3))
        x = statistics.mean(average_data)
        ca = abs((x - specification_center) / (t / 2))
        stdev = statistics.stdev(average_data)  # 標準差
        # stdev = 0.1
        cp = (upper_limit - lower_limit) / (6 * stdev)
        cpk = cp * (1 - ca)
        # print(cpk)
        # print(ca)
        # print(cp)
        # --------------------------------------------顏色判別
        ca_color = str()
        cpk_color = str()
        cp_color = str()
        ca_, cp_, cpk_ = cpk_check(ca, cp, cpk)
        data = {'item_name': item['measurement_items'], 'cp': round(cp, 3), 'ca': round(ca, 3), 'cpk': round(cpk, 3),
                'ca_': ca_, 'cp_': cp_, 'cpk_': cpk_}
        # print(data)
        cpk_data.append(data)
    print(cpk_data)
    cpk_data = [
        {'item_name': '示範項目1', 'cp': 16.667, 'ca': 0.12, 'cpk': 14.667, 'ca_': ['A+', '製程穩定'], 'cp_': ['A+', '製程穩定'],
         'cpk_': ['A+', '製程穩定']},
        {'item_name': '示範項目2', 'cp': 5.774, 'ca': 0.233, 'cpk': 4.426, 'ca_': ['A', '製程穩定'], 'cp_': ['A+', '製程穩定'],
         'cpk_': ['A+', '製程穩定']}]
    message = str()

    for item in cpk_data:
        message = message + '量測項目：' + str(item['item_name']) + '\n' + \
                  '   ' +'製成能力(Ca)：' + str(item['ca']) + '   ' + '製成能力等級：' + item['ca_'][0] +'  ' +item['ca_'][1] +'\n' + \
                  '   ' +'製成準確度(Cp)：' + str(item['cp']) + '   ' + '製成準確度等級：' + item['cp_'][0] +'  '+ item['ca_'][1] +'\n' + \
                  '   ' +'製成能力指數(Cpk)：' + str(item['cpk']) + '   ' + '製成能力指數等級：' + item['cpk_'][0]+'  ' + item['ca_'][1] +'\n'

    print(message)
    # send_('嗨', message, ['c108105112@nkust.edu.tw', 'c109104260@nkust.edu.tw', 'c109105113@nkust.edu.tw'])
    # send_('嗨', message, ['f110102125@nkust.edu.tw'])

    # word_order = models.work_order_measure_items.measurement_work_order.objects(id=latest_measure_work_order_id)
    # word_order_name = word_order


def send_(subject, message, mail):
    from django.conf import settings
    from django.core.mail import send_mail
    # subject = 'welcome to GFG world'
    # message = f'Hi , thank you for registering in geeksforgeeks.'
    email_from = settings.EMAIL_HOST_USER
    recipient_list = mail
    send_mail(subject, message, email_from, recipient_list)
    print('sucess send')

# from email.mime.multipart import MIMEMultipart
# from email.mime.multipart import MIMEMultipart
# from email.mime.text import MIMEText
#
# content = MIMEMultipart()  # 建立MIMEMultipart物件
# content["subject"] = "嗨"  # 郵件標題
# content["from"] = "a20202042@gmail.com"  # 寄件者
# content["to"] = "c108105112@nkust.edu.tw"  # 收件者
# content.attach(MIMEText("Demo python send email"))  # 郵件內容
#
# import smtplib
#
# for i in range(0, 100):
#     with smtplib.SMTP(host="smtp.gmail.com", port="587") as smtp:  # 設定SMTP伺服器
#         try:
#             smtp.ehlo()  # 驗證SMTP伺服器
#             smtp.starttls()  # 建立加密傳輸
#             smtp.login("a20202042@gmail.com", "gstxpmjbqxkfljox")  # 登入寄件者gmail
#             smtp.send_message(content)  # 寄送郵件
#             print("Complete!")
#         except Exception as e:
#             print("Error message: ", e)
