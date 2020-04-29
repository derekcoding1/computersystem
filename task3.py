#!/usr/bin/env python
# coding: utf-8

# In[9]:


import re
from pyspark.sql import SparkSession
from pyspark.sql.types import StringType
from pyspark.sql.types import ArrayType
from pyspark.sql.functions import lower, udf, col
from pyspark.sql.functions import explode


# In[3]:


spark = SparkSession.builder.getOrCreate()
df = spark.read.format('xml').options(rowTag='page').load('hdfs:/enwiki_small.xml')


# In[2]:


def internal_links(row):
    '''
    INPUT: x is a row of the spark dataframe
    '''
    X = re.findall(r'\[\[(.*?)\]\]',row['text']['_VALUE'].lower())
    list0 = []
    for i in X:
        if "#" not in i:
            if ":" in i:
                if "category:" in i:
                    list0.append(i.split('|')[0].strip())
            else:
                list0.append(i.split('|')[0].strip())
    return list0


# In[4]:


inter_link_list = udf(lambda y: internal_links(y), ArrayType(StringType()))


# In[22]:


def get_table(df,inter_link_list):
    temp = df.withColumn("revision_list",inter_link_list(col('revision'))) #.show()
    df2 = temp.select(lower(col('title')).alias("title"),explode(temp.revision_list).alias("revision"))
    return df2.orderBy("title","revision",ascending=True)


# In[23]:


t2 = get_table(df,inter_link_list)


# In[24]:


t2.show()


# In[ ]:


t3 = t2.groupBy('title').count().orderBy("title",ascending=True)


# In[26]:


t3 = t2.groupBy('title').count().orderBy("title",ascending=True)

