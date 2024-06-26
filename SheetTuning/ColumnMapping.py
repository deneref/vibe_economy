ColumnMapping = {
    'allocatedSpending': {
        'Продукт': 'product_nm',
        'Номер поставки': 'supply_id',
        'Категория': 'category',
        'Аллоцированный Расход':  'allocated_amt',
        'Комментарий': 'comment'
    },
    'opEx': {
        'Номер поставки': 'supply_id',
        'Категория': 'category',
        'Общий расход': 'item_amt'
    },
    'capEx': {
        'Наименование': 'name',
        'Сумма': 'item_amt'
    },
    'supply': {
        'Номер поставки': 'supply_id',
        'Продукт': 'product_nm',
        'Едениц': 'supply_amt'
    },
    'investments': {

    },
    'result': {

    },
    'remains': {
        'Номер поставки': 'supply_id',
        'Продукт': 'product_nm',
        'Едениц': 'supply_amt'
    },
    'sales': {
        'Номер поставки': 'supply_id',
        'Продукт': 'product_nm',
        'Канал': 'channel',
        'Стоимость': 'item_amt',
        'Дата': 'sale_date'
    },
    'marketing':
    {
        'Номер кампании': 'campany_id',
        'Канал': 'channel',
        'Сумма': 'item_amt',
        'Продукт': 'product_nm',
        'Номер маркетинговой кампании': 'campany_id',
        'Дата начала': 'start_dt',
        'Дата окончания': 'end_dt'
    }
}
