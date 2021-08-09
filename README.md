# PyGalaxy

This is a simple common package. 

Github: https://github.com/patrickxu1986/pygalaxy

#### Dependence

```python
pip3 install -r requirements.txt
```

#### Use

-  logger

```python
from pygalaxy import logger

logger.debug('log message') 
logger.info('log message') 
```

-  time_master

```python
from pygalaxy import time_master

time_master.get_current_date_str()
time_master.get_current_unix_time()
```

-  consistent hash

```python
from pygalaxy.consistent_hash import Node, ConsistentHash

node = Node(node_name='192.1.1.4')
consistent_hash = ConsistentHash()
consistent_hash.add_node(node)
n = consistent_hash.get_node('test content')

```

-  aes master

```python
from pygalaxy.aes_master import AesMaster

encrypt = AesMaster.encrypt('test content', key='this is a key')
print(encrypt)
decrypt = AesMaster.decrypt(encrypt, key='this is a key')
print(decrypt)
```
