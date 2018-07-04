# _*_ coding:utf-8 _*_
import cx_Oracle
import sys
import calendar
from pyecharts import Bar,Line

conn = cx_Oracle.connect('panda/Panda_Auto1024@116.62.196.190/orcl')
cursor = conn.cursor()


def get_fee(time):
    sql = ("select count(bo.TOTAL_AMOUNT) from panda.biz_order bo left join panda.biz_order_item boi "
           "on bo.ORDER_NO = boi.ORDER_NO "
           "where boi.REAL_GET_TIME "
           "between to_date('2018/06/" + str(time) + " 00:00:00', 'yyyy/MM/dd hh24:mi:ss')"
           "and to_date('2018/06/" + str(time) + " 23:59:59', 'yyyy/MM/dd hh24:mi:ss')"
           )

    cursor.execute(sql)
    total_fee = cursor.fetchone()
    return total_fee


fee_list = [13476, 13882, 13540, 11566, 11894, 11817, 11913, 12763, 14156, 13550, 10444, 11664, 12255, 12795, 14201, 14835, 14313, 14459, 11597, 11865, 12581, 13909, 14451, 13683, 11425, 11446, 11730, 11818, 12508, 13814]

#for i in range(30):
#    day = i + 1
#   fee_list.append(get_fee(day)[0])
#print fee_list
attr = [i+1 for i in range(30)]
bar = Line("订单数量", "按天统计")
bar.add("订单量", attr, fee_list, mark_line=["average"], mark_point=["max", "min"])
bar.render(r"line.html")