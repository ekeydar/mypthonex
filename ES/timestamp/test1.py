import elasticsearch
import logging,logging.config
import inplay_common.utils
import datetime
import pytz
import time

logging.config.dictConfig({
    'version' : 1,
    'disable_existing_loggers' : False,
    'handlers': {
        'console' : {
            'level' : 'INFO',
            'class' : 'logging.StreamHandler',
            'formatter' : 'short',
        }
    },
    'formatters' : {
        'short' : {
            'format': '[%(asctime)s] %(message)s',
            'datefmt' : '%H:%M:%S'
        }
    },
    'loggers': {
        'output' : {
            'handlers' : ['console'],
            'level' : 'DEBUG',
            'propagate' : False
        },
    }
});

LOGGER = logging.getLogger('output')

ES = elasticsearch.Elasticsearch()

def main():
    create_index()
    find_on_dates()

def find_on_dates():
       body = {
           "query": {
               "filtered": {
                   "filter": {
                       "range": {
                           "created_at": {
                               "gt": '2015-02-11',
                               "lt": '2015-02-15',
                           }
                       }
                   }
               }
           }
       }
       result = ES.search(index='ts1',
                          doc_type='docs',
                          body=body,
                          size=1000)
       print 'Found %s docs:' % (result['hits']['total'])
       for idx,hit in enumerate(result['hits']['hits']):
           source = hit['_source']
           dt = datetime.datetime(year=source['year'],
                                  month=source['month'],
                                  day=source['day'],
                                  hour=source['hour'],
                                  minute=source['minute'],
                                  second=source['second'],
                                  microsecond=source['microsecond'])
           print '%s) %s' % (idx,dt.isoformat())
       return result

def create_index():
    if ES.indices.exists('ts1'):
        ES.indices.delete('ts1')
    mappings = {
        "docs" : {
            "_source" : {
                "includes" : ["*"]
            },
            "transform" : {
                "script" : "ctx._source['created_at'] = ctx._source['created_at'].toLong() * 1000",
                "lang": "groovy"
            },
            "properties" : {
                "created_at" : {"type" : "date"},
            }
        }
    }
    ES.indices.create('ts1',body=dict(mappings=mappings))
    LOGGER.info('index created')
    for month in xrange(1,13):
        for day in xrange(1,25):
            params = dict(year=2015,month=month,day=day,hour=10,minute=11,second=12,microsecond=131415)
            dt = datetime.datetime(tzinfo=pytz.UTC,**params)
            created_at = inplay_common.utils.time_to_timestamp(dt)
            doc_id = '%s-%s' % (month,day)
            ES.index(index='ts1',
                     doc_type='docs',
                     id=doc_id,
                     body=dict(created_at=created_at,
                               **params))
    LOGGER.info('waiting for index')
    while True:
        time.sleep(0.1)
        count = ES.count(index='ts1',doc_type='docs')['count']
        LOGGER.info('%s so far' % count)
        if count > 270:
            break
    
    
if __name__ == '__main__':
    main()
