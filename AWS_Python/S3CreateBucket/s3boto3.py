import boto3
import pprint
# a standard library to
from PIL import Image


def retrieve_properties():
    prop_data = []
    with open("AWS_Config.properties", 'r') as AWS_PROP:
        for each_line in AWS_PROP:
            prop_data.append(each_line.rstrip())
    return prop_data


def create_s3_bucket():
    aws_keys = retrieve_properties()
    access_key = aws_keys[0].split("=")[1]
    serect_key = aws_keys[1].split("=")[1]
    client = boto3.client("s3", aws_access_key_id=access_key, aws_secret_access_key=serect_key)
    # @https://stackoverflow.com/questions/31092056/how-to-create-a-s3-bucket-using-boto3
    """ :type : pyboto3.s3 """
    client.create_bucket(Bucket='my-python-s3', CreateBucketConfiguration={'LocationConstraint': 'us-west-2'})


def list_s3_bucket():
    aws_keys = retrieve_properties()
    access_key = aws_keys[0].split("=")[1]
    serect_key = aws_keys[1].split("=")[1]
    client = boto3.client("s3", aws_access_key_id=access_key, aws_secret_access_key=serect_key)
    """ :type : pyboto3.s3 """
    response = client.list_buckets()
    pprint.pprint(response.get('Buckets'))


def upload_data_to_s3_bucket(file_name, bucket, object_name=None, args=None):
    """
    :param file_name: name of file on local
    :param bucket: bucket name
    :param object_name: name of file to be in S3 (None) then using local file_name
    :param args: custom args
    :return:
    """
    # set object_name to local file_name if not passed as arg
    if object_name == None:
        object_name = file_name
    aws_keys = retrieve_properties()
    access_key = aws_keys[0].split("=")[1]
    serect_key = aws_keys[1].split("=")[1]
    client = boto3.client("s3", aws_access_key_id=access_key, aws_secret_access_key=serect_key)
    """ :type : pyboto3.s3 """
    response = client.upload_file(file_name, bucket, object_name, ExtraArgs= args)
    # respones should be None otherwise exception
    pprint.pprint(response)


def download_file_from_s3():
    aws_keys = retrieve_properties()
    access_key = aws_keys[0].split("=")[1]
    serect_key = aws_keys[1].split("=")[1]
    client = boto3.client("s3", aws_access_key_id=access_key, aws_secret_access_key=serect_key)
    """ :type : pyboto3.s3 """
    target_bucket = "my-python-s3"
    # print(client.get_object(Bucket=target_bucket, Key="00-puppy.jpg"))
    client.download_file(Bucket=target_bucket, Key="00-puppy.jpg", Filename="download_from_s3.jpg")


def main():
    # #######################################################
    # create bucket Checked
    # create_s3_bucket()
    # #######################################################
    # #######################################################
    # list out existing buckets Checked
    list_s3_bucket()
    # #######################################################

    # #######################################################
    # upload files into S3 bucket Checked
    #target_file_path = '/Users/junpark/Downloads/Computer-Vision-with-Python/DATA/00-puppy.jpg'
    # to make it dynamic use uuid + split("/") and use last data of the list
    # upload_data_to_s3_bucket(target_file_path, 'my-python-s3', "00-puppy.jpg")
    # #######################################################
    download_file_from_s3()


if __name__ == "__main__":
    main()