import vcr

yauta_vcr = vcr.VCR(
    serializer='yaml',
    cassette_library_dir='tests/fixtures/cassettes',
    record_mode='once',
    match_on=['uri', 'method'],
    filter_headers=[('Authorization', 'TESLA_ACCESS_TOKEN')],
    filter_post_data_parameters=[
        ('client_id', 'TESLA_CLIENT_ID'),
        ('client_secret', 'TESLA_CLIENT_SECRET'),
        ('email', 'TESLA_EMAIL'),
        ('password', 'TESLA_PASSWORD'),
        ('pin', 'TESLA_PIN')
    ]
)


__all__ = [yauta_vcr]
