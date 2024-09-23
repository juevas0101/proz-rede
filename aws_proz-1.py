import boto3
import os


instance_id = 'i-879078fjjf84'  
volume_id = 'vol-7g8h9f0e1d3c4b5ax'    
file_path = 'caminho/do/seu/arquivo.txt'  

ec2 = boto3.client('ec2')

volumes = ec2.describe_volumes(VolumeIds=[volume_id])
attached = volumes['Volumes'][0]['Attachments'][0]
if attached['State'] == 'attached':
    print(f"O volume {volume_id} está anexado à instância {instance_id}.")
    
    
    os.system(f"scp -i /caminho/para/sua/chave.pem {file_path} ec2-user@{attached['InstanceId']}:/caminho/de/destino/no/ebs/")
    print(f"Arquivo {file_path} enviado para a instância EC2.")
else:
    print(f"O volume {volume_id} não está anexado.")
