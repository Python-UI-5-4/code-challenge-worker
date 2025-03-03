from common import get_env_var


class DockerConfig:
    """
    Description:
        Docker 설정 정보를 관리하는 클래스.
    """
    DOCKER_IMAGE = {
        "java17": get_env_var("SANDBOX_IMAGE_JAVA17"),
        "nodejs": get_env_var("SANDBOX_IMAGE_NODEJS20"),
        "nodejsesm": get_env_var("SANDBOX_IMAGE_NODEJS20"),
    }
