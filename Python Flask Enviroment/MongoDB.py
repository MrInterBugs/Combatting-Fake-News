import pymongo

myclient = pymongo.MongoClient("mongodb://localhost:27017/")

mydb = myclient["fakeNews"]
mycol = mydb["privateKeys"]

mydict = { "ID": "BBC", "privateKey": "-----BEGIN RSA PRIVATE KEY-----\nMIIEowIBAAKCAQEAqZTTsah8PCiLU4ZwzYs7ODJ1qZ4aSKlRwyqAwygsPPAv6CE8\n3ccDS1P1VWV9nM1Dzo4tYJHNladxx+tIbtairgLc8YJBdGj8cUjvZqIaw4zTUc2c\noaOvmVCNUXKPqbLPSpiNU4q09P864g4nS6/+su6/h1JJhopDUSAeT1JQFjnGaS/Z\nZzfJ6ZpwTcnefPrqXRae78erkmLohRPDC7ijGX+9OJ5Jh662OStzzp/ArSbKxeFt\n38xBE2McKGfcxnTOeW+pSL22vJupK2DWAVA38uOM+c9fwB/fvXb1dhZ+4BbW36p3\niCd4L/xsgl2ZdC1lOLh9+U2hkke6X7Tby4JCrwIDAQABAoIBADSEaqrySsc2py9O\ny1BcdhKJTfchh3JJPZD7cLT/k/OrTqrM4FSudU62yZuQur38s6scTOFDRi+6k3oe\nW2g4AFlzeYkxlaO/f651r+5Q9Yjp6+fBjWhhkNgiIiG/IM6lGZ04cUwWAMR+5nVr\nfK/r6Szw00/NJAgOeZp+H+Tg0PyQlq4QanzgeJVJZNGc/bGK+nm+n5H13k2JCkq3\nst0j65U6PhTFqG7DBTyx9QzmuCiU9HxxaHJ8RJRF1kVtkIFISW0UILmjz6Jx6glT\nrz4wqIKgspbyo32qiDf3/bokJY/Psvt9yifG3bYn0cw2IRDlFEQgKMFQoTlLidl/\nHTUA38ECgYEA26NOlg/T7bt1pA3CGTOKQIzLnclqgTs2ITzqSB5pkqciACAIUAem\nB/UDJCFvpQKJzUnn1wp0bRZ8x9+2qYPyTNL7sElxyf2zwksCigScu2IoycMkOiWh\n8HJ4Y4fcBT5SbmLaWf16zcuY9uFdhhYOSRcdWHxZWloM0PAZ9aztS+0CgYEAxagF\n4pspd5rLkeNgEpmNK1FwhnCp2eADNQVWNlmypmEjeUybQcteGSFBAuaoOVeArCLM\n023atzkCcziZg2TosM6LNXfsc3pe6kQxloiPE2EWHjxasY6cIeqgQF8Eshb0TbUC\nGAXEgt/UEmMLaVo1pdqDEbEa/orp2B4Pdl0rDYsCgYEAsih9jmu4VJZCjpg6YYbV\nFhce8xZ2Ne15suxefbFtoW/AvKk/FOufWcT8j0ov7YFplgPk8yGf3vzmqppk6IwG\n9xoM3qo0iswoC+ocXSfwmm689yw7Lo9oFEpGLTX+2qH66190Dpr2CgikQ137JtCt\nNcxyGVyEfi2dR7360LU8puECgYBxW4XUioxjrgFmL/Mfd7UAzPouAFtJOzJbrC3f\nid3tkfRYUtkQCOR0oR+53DNKf6aqEmNKNsyjHC0Ni75vHuZc0HgCOD8Bk4Lv9CBE\nZxk3UgzvVknlXxaoVPmHMXdt88A0+MS0pkonjNsBmJAo4bW24vUcpmgG6ABpFARm\nK9TPNQKBgCkdQ9Yj9uKSaNA97Px5kaF7LhI//5OhZ1ogPiadKAQuiF9K2H3Vr3TZ\nDbeivpY1GZQTKUUuSfDm5PUjuNhqWp0evRY1aU8ctE/UqV+Jl76m+LVJKAXrqzHi\nR5R/yHsn+nu87MhHU3on02FkJNPGl9oClxe7462DDuLJ8Fy1Fv/6\n-----END RSA PRIVATE KEY-----"}

x = mycol.insert_one(mydict)

print(x.inserted_id)