from shortcuts.template import render
from app.split import PositionSplit


def register(val):
    """
    :param val: original data format to Dicts from terminal!
    :return: a render which a tuple factory
    you should know what you are doing and which field you need!
    """
    template = 'client_msg_id|client_msg_attr|client_dev_id|client_msg_product|client_content'
    return render(val, template)


def auth(val):
    msg_content = 'client_msg_product|client_msg_id|sys_ok'
    template = 'ser_com_rsp|sys_fixed_msg_attr|client_dev_id|sys_product|' + msg_content
    return render(val, template)


def position(val):
    content = val['client_content']
    position_instance = PositionSplit(content)
    for item in position_instance.hash_data:
        print 'key [%s]    value [%s]' % (item, position_instance.hash_data[item])
        #
        # print 'gps datetime     :', position_instance.hash_data['datetime']
        # print 'gps longitude     :', position_instance.hash_data['longitude']
        # print 'gps latitude     :', position_instance.hash_data['latitude']
        # print 'gps altitude     :', position_instance.hash_data['altitude']
        # print 'gps speed     :', position_instance.hash_data['speed']


if __name__ == '__main__':
    """
    The below sample dicts just for test the register!
    """
    request = {'msg_id': (1, 2), 'msg_attr': (0, 2), 'dev_id': (153, 17, 152, 64, 130, 104), 't_product': (0, 1),
               'content': (81, 82), 'crc': (185,)}
    example = auth(request)
    print 'example      :', example
