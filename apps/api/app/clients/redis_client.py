import redis.asyncio as redis

from app.config.settings import settings

RedisClient = redis.Redis


def create_redis_client() -> RedisClient:
    return RedisClient(
        host=settings.redis.HOST,
        port=settings.redis.PORT,
        username=settings.redis.USERNAME,
        password=settings.redis.PASSWORD,
    )
