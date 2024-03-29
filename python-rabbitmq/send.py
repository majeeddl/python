from sqlite3 import connect
import pika

credentials = pika.PlainCredentials('admin', 'admin')

connection = pika.BlockingConnection(pika.ConnectionParameters(host='localhost',credentials=credentials))

channel = connection.channel()

channel.queue_declare(queue="hello")

channel.basic_publish(exchange='', routing_key='hello', body='Hello World!')

print(" [x] sent 'Hello World!'")

connection.close()