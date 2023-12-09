
# This file contains all the paths for the API calls
# Paths
paths = {
    # User
    'users': {
        'login': '/users/login',
        'register': '/users/register',
        'logout': '/users/logout',
        'change_password': '/users/changepassword'
    },
    # Crops
    'crops': {
        'search': '/crops/searchCrops',
        'get_list': '/crops/getCropList',
        'get_details': '/crops/getCropDetails'
    },
    # News
    'news': {
        'search': '/news/searchNews',
        'get_list': '/news/getNewsList'
    },
    # Schedule
    'schedules': {
        'add': '/schedules/addSchedule',
        'edit': '/schedules/updateSchedule',
        'delete': '/schedules/deleteSchedule',
        'get_details': '/schedules/getScheduleDetails',
        'get_list': '/schedules/getScheduleList'
    },
    # Government Policies
    'governmentPolicies': {
        'search': '/governmentPolicies/searchPolicy',
        'get_details': '/governmentPolicies/getPolicyDetails',
        'get_list': '/governmentPolicies/getPolicyList'
    },
    # Market Place
    'marketPlace': {
        'add_product': '/marketPlace/addProduct',
        'edit_product': '/marketPlace/editProduct',
        'delete_product': '/marketPlace/deleteProduct',
        'search_product': '/marketPlace/searchProduct',
        'get_details': '/marketPlace/getProductDetails',
        'get_trending': '/marketPlace/getTrendingProducts',
        'get_user_products': '/marketPlace/getUserProducts'
    },
    # Activity
    'activity': {
        'activity': '/activity/activity'
    }
}

