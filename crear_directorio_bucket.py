import boto3

def lambda_handler(event, context):
    # Entrada (json)
    nombre_bucket = event['body']['bucket']
    nombre_dir = event['body']['dir'] + '/'
    
    # Proceso    
    s3 = boto3.resource('s3')
    bucket = s3.Bucket(nombre_bucket)
    k = bucket.put_object(Key=nombre_dir)

    return {
        'statusCode': 200,
        'bucket': nombre_bucket,
        'dir': nombre_dir
    }
