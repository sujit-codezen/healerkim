# Simple UI
SIMPLEUI_LOGO = 'https://i.ibb.co/1fQJd42/logo.png'
SIMPLEUI_STATIC_OFFLINE = True
SIMPLEUI_HOME_ACTION = False
SIMPLEUI_HOME_INFO = False
SIMPLEUI_HOME_QUICK = True
SIMPLEUI_DEFAULT_THEME = 'e-green-pro.css'
SIMPLEUI_HOME_ICON = 'fa fa-user'
SIMPLEUI_DEFAULT_ICON = False
SIMPLEUI_LOADING = False
SIMPLEUI_ANALYSIS = False
SIMPLEUI_LOADING = True
SIMPLEUI_CONFIG = {
    'dynamic':
    True,
    'system_keep':
    False,
    'menus': [
        {
            'app':
            'auth',
            'icon':
            'fa fa-users',
            'name':
            'Users',
            'models': [
                {
                    'name': 'Users',
                    'icon': 'fa fa-users',
                    'url': 'users/user/'
                },
                {
                    'name': 'OTP',
                    'icon': 'fa fa-users',
                    'url': 'users/phoneotp/'
                },
            ],
        },
        {
            'app':
            'auth',
            'icon':
            'fa fa-cutlery',
            'name':
            'Restaurants',
            'models': [
                {
                    'name': 'Restaurants',
                    'icon': 'fa fa-cutlery',
                    'url': 'restaurants/restaurant/'
                },
            ],
        },
        {
            'app':
            'auth',
            'icon':
            'fa fa-asterisk',
            'name':
            'Menus',
            'models': [
                {
                    'name': 'Menus',
                    'icon': 'fa fa-asterisk',
                    'url': 'menus/menu/'
                },
            ],
        },
        {
            'app':
            'auth',
            'icon':
            'fa fa-shopping-bag',
            'name':
            'Orders',
            'models': [
                {
                    'name': 'Orders',
                    'icon': 'fa fa-shopping-bag',
                    'url': 'orders/order/'
                },
            ],
        },
    ]
}