def convert_pg_uri(old_uri: str) -> str:
    if 'postgres:' in old_uri:
        return old_uri.replace('postgres', 'postgresql')
    else:
        return old_uri
