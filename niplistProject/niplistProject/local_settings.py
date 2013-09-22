FACEBOOK_APP_ID              = '519431724811205'
FACEBOOK_API_SECRET          = '7af55b5536e04f05a13feaffd419e75d'

SOCIAL_AUTH_CREATE_USERS          = True
SOCIAL_AUTH_FORCE_RANDOM_USERNAME = False
SOCIAL_AUTH_DEFAULT_USERNAME      = 'socialauth_user'
SOCIAL_AUTH_COMPLETE_URL_NAME     = 'socialauth_complete'
SOCIAL_AUTH_ERROR_KEY             = 'socialauth_error'

# Used by the authentication system for the private-todo-list application.
# URL to use if the authentication system requires a user to log in.
LOGIN_URL = '/niplist/login'
LOGIN_ERROR_URL    = '/niplist/login-error/'
# Default URL to redirect to after a user logs in.
LOGIN_REDIRECT_URL = '/niplist/newsfeed'

SOCIAL_AUTH_FORCE_POST_DISCONNECT = True

SOCIAL_AUTH_PIPELINE = (
    'social_auth.backends.pipeline.social.social_auth_user',
    'social_auth.backends.pipeline.associate.associate_by_email',
    'social_auth.backends.pipeline.misc.save_status_to_session',
    'app.pipeline.redirect_to_form',
    'app.pipeline.username',
    'social_auth.backends.pipeline.user.create_user',
    'social_auth.backends.pipeline.social.associate_user',
    'social_auth.backends.pipeline.social.load_extra_data',
    'social_auth.backends.pipeline.user.update_user_details',
)
