from app.controllers.home_controller import home_bp
from app.api.api_heladeria import api_bp
# from app.api.api_heladeria_deploy import api_deploy_bp

def registrar_rutas(app):
    app.register_blueprint(home_bp)
    app.register_blueprint(api_bp)
    # app.register_blueprint(api_deploy_bp)