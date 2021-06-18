import boto3
from botocore.exceptions import ClientError

# Reference Documentation:
# @https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/DAX.client.run-application-python.01-create-table.html

def retrieve_properties():
    prop_data = []
    with open("AWS_Config.properties", 'r') as AWS_PROP:
        for each_line in AWS_PROP:
            prop_data.append(each_line.rstrip())
    return prop_data


def create_dynamodb_table():
    aws_keys = retrieve_properties()
    access_key = aws_keys[0].split("=")[1]
    serect_key = aws_keys[1].split("=")[1]
    boto3_dynamodb = boto3.resource('dynamodb', region_name='us-west-2', aws_access_key_id=access_key,
                        aws_secret_access_key=serect_key)
    # @https://stackoverflow.com/questions/31092056/how-to-create-a-s3-bucket-using-boto3
    """ :type : pyboto3.dynamodb """
    print(list(boto3_dynamodb.tables.all()))
    # param for create table
    table_name = "MoviePython"
    try:
        params = {
            'TableName': table_name,
            # list of dictionary
            'KeySchema' :[
                {'AttributeName': 'partition_key', 'KeyType': 'HASH'},
                {'AttributeName': 'sort_key', 'KeyType': 'RANGE'}
            ],
            'AttributeDefinitions': [
                {'AttributeName': 'partition_key', 'AttributeType': 'N'},
                {'AttributeName': 'sort_key', 'AttributeType': 'N'}
            ],
            'ProvisionedThroughput': {
                'ReadCapacityUnits': 10,
                'WriteCapacityUnits': 10
            }
        }
        table = boto3_dynamodb.create_table(**params)
        print(f"Creating table...")
        table.wait_until_exists()
        return table
    except ClientError:
        print("Table already exist")



def main():
    movie_table = create_dynamodb_table()

    pass


if __name__ == "__main__":
    main()