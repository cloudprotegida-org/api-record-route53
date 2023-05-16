from flask import Flask
import boto3

app = Flask(__name__)

@app.route('/create-record/<name>')
def create_record(name):
    route53 = boto3.client('route53')

    zone_id = 'ADD HOSTED ZONE ID'

    response = route53.change_resource_record_sets(
        HostedZoneId=zone_id,
        ChangeBatch={
            'Changes': [
                {
                    'Action': 'CREATE',
                    'ResourceRecordSet': {
                        'Name': name + '.minhapp.com.br',
                        'Type': 'A',
                        'TTL': 300,
                        'ResourceRecords': [
                            {
                                'Value': '10.20.30.40'
                            }
                        ]
                    }
                }
            ]
        }
    )

    return 'Registro criado com sucesso!'

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
