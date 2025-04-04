import redis

# Configure Redis client
redis_client = redis.StrictRedis(host='localhost', port=6379, db=0)

def get_url_from_cache(url, cache_type='whitelist'):
    """Check if URL is in cache"""
    if cache_type == 'whitelist':
        return redis_client.sismember('whitelist', url)
    elif cache_type == 'blacklist':
        return redis_client.sismember('blacklist', url)
    return False
