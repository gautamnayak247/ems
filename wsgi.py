from app import init_app
from config import Config

cnfg = Config()
ems_app = init_app(cnfg)

if __name__ == "__main__":
    ems_app.run(host=cnfg.Host, port=cnfg.Port, debug=cnfg.Debug)
