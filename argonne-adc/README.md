# Argonne Library

## Configuring library 1.0: 
### Setup like develop or try
```
pip install virtualenv
virtualenv adc
pip install lib/adc-0.0.1-py3-none-any.whl

```


### Available **adc** commands:
```
adc-me

adc-auth

adc-users

adc-user

adc-showToken

adc-studies

adc-study

adc-create-study

adc-create-sample

adc-samples

adc-sample

adc-invs

adc-inv

adc-create-inv

```

## How to use the Library: 
### Commands

## How to use the SDK: 
### Commands

#### $ adc-me

This command is used to check your user and the information linked to it. 

###### sample output:

```json
$ adc-me
python main.py me
This is your response:
{"data":{"me":{"id":"VXNlck5vZGU6MQ==","username":"gonzalo.martinez@domandtom.com","email":"gonzalo.martinez@domandtom.com","studies":[],"investigations":[{"id":"SW52ZXN0aWdhdGlvbk5vZGU6Ng==","name":"Test Study Name","description":"Test Study Description","samples":[]},{"id":"SW52ZXN0aWdhdGlvbk5vZGU6Nw==","name":"Test Study Name","description":"Test Study Description","samples":[{"name":"Test Sample 2","url":"/media/uploads/simplified_sample_8JF3Ryx.json"}]}],"samples":[]}}}

```
***
#### $ adc-users

This command will return an array of users and the information linked to them.
###### sample output:

```json
$ adc-users
python main.py users
This is your response:
{"data":{"users":{"edges":[{"node":{"id":"VXNlck5vZGU6MQ==","username":"gonzalo.martinez@domandtom.com","email":"gonzalo.martinez@domandtom.com","created":"2021-07-22T14:22:10.308545+00:00","updated":"2021-07-22T14:22:10.308568+00:00","investigations":[{"id":"SW52ZXN0aWdhdGlvbk5vZGU6Ng==","name":"Test Study Name","keywords":["test","graphql","demo","argonne"]},{"id":"SW52ZXN0aWdhdGlvbk5vZGU6Nw==","name":"Test Study Name","keywords":["test","graphql","demo","argonne"]}],"samples":[],"studies":[]}},{"node":{"id":"VXNlck5vZGU6Mg==","username":"sherry38","email":"mayodeanna@williamson.com","created":"2021-07-22T14:24:24.826227+00:00","updated":"2021-07-22T14:24:24.826238+00:00","investigations":[{"id":"SW52ZXN0aWdhdGlvbk5vZGU6MQ==","name":"Test Investigation 0","keywords":["Keyword 0","Keyword 1","Keyword 2","Keyword 3","Keyword 4"]}],"samples":[{"name":"Test Sample 1","id":"U2FtcGxlTm9kZTox","url":"/media/uploads/simplified_sample.json","keywords":["Keyword 0","Keyword 1","Keyword 2","Keyword 3","Keyword 4"]}],"studies":[{"id":"U3R1ZHlOb2RlOjE=","name":"Test Study 0","investigations":[{"id":"SW52ZXN0aWdhdGlvbk5vZGU6MQ==","name":"Test Investigation 0","keywords":["Keyword 0","Keyword 1","Keyword 2","Keyword 3","Keyword 4"]},{"id":"SW52ZXN0aWdhdGlvbk5vZGU6Ng==","name":"Test Study Name","keywords":["test","graphql","demo","argonne"]},{"id":"SW52ZXN0aWdhdGlvbk5vZGU6Nw==","name":"Test Study Name","keywords":["test","graphql","demo","argonne"]}],"keywords":["Keyword 0","Keyword 1","Keyword 2","Keyword 3","Keyword 4"]}]}},{"node":{"id":"VXNlck5vZGU6Mw==","username":"combsashlee","email":"carrillopatrick@hotmail.com","created":"2021-07-22T14:24:24.842762+00:00","updated":"2021-07-22T14:24:24.842770+00:00","investigations":[{"id":"SW52ZXN0aWdhdGlvbk5vZGU6Mg==","name":"Test Investigation 1","keywords":["Keyword 0","Keyword 1","Keyword 2","Keyword 3","Keyword 4"]}],"samples":[{"name":"Test Sample 2","id":"U2FtcGxlTm9kZToy","url":"/media/uploads/simplified_sample_8JF3Ryx.json","keywords":["Keyword 0","Keyword 1","Keyword 2","Keyword 3","Keyword 4"]}],"studies":[{"id":"U3R1ZHlOb2RlOjI=","name":"Test Study 1","investigations":[{"id":"SW52ZXN0aWdhdGlvbk5vZGU6Mg==","name":"Test Investigation 1","keywords":["Keyword 0","Keyword 1","Keyword 2","Keyword 3","Keyword 4"]}],"keywords":["Keyword 0","Keyword 1","Keyword 2","Keyword 3","Keyword 4"]}]}},{"node":{"id":"VXNlck5vZGU6NA==","username":"mmckay","email":"peggyspears@yahoo.com","created":"2021-07-22T14:24:24.850336+00:00","updated":"2021-07-22T14:24:24.850343+00:00","investigations":[{"id":"SW52ZXN0aWdhdGlvbk5vZGU6Mw==","name":"Test Investigation 2","keywords":["Keyword 0","Keyword 1","Keyword 2","Keyword 3","Keyword 4"]}],"samples":[{"name":"Test Sample 3","id":"U2FtcGxlTm9kZToz","url":"/media/uploads/simplified_sample_UYlPLPB.json","keywords":["Keyword 0","Keyword 1","Keyword 2","Keyword 3","Keyword 4"]}],"studies":[{"id":"U3R1ZHlOb2RlOjM=","name":"Test Study 2","investigations":[{"id":"SW52ZXN0aWdhdGlvbk5vZGU6Mw==","name":"Test Investigation 2","keywords":["Keyword 0","Keyword 1","Keyword 2","Keyword 3","Keyword 4"]}],"keywords":["Keyword 0","Keyword 1","Keyword 2","Keyword 3","Keyword 4"]}]}},{"node":{"id":"VXNlck5vZGU6NQ==","username":"rfuller","email":"peterscristina@hotmail.com","created":"2021-07-22T14:24:24.856984+00:00","updated":"2021-07-22T14:24:24.856990+00:00","investigations":[{"id":"SW52ZXN0aWdhdGlvbk5vZGU6NA==","name":"Test Investigation 3","keywords":["Keyword 0","Keyword 1","Keyword 2","Keyword 3","Keyword 4"]}],"samples":[{"name":"Test Sample 4","id":"U2FtcGxlTm9kZTo0","url":"/media/uploads/simplified_sample_qANM8An.json","keywords":["Keyword 0","Keyword 1","Keyword 2","Keyword 3","Keyword 4"]}],"studies":[{"id":"U3R1ZHlOb2RlOjQ=","name":"Test Study 3","investigations":[{"id":"SW52ZXN0aWdhdGlvbk5vZGU6NA==","name":"Test Investigation 3","keywords":["Keyword 0","Keyword 1","Keyword 2","Keyword 3","Keyword 4"]}],"keywords":["Keyword 0","Keyword 1","Keyword 2","Keyword 3","Keyword 4"]}]}},{"node":{"id":"VXNlck5vZGU6Ng==","username":"kentsanchez","email":"icabrera@gmail.com","created":"2021-07-22T14:24:24.861936+00:00","updated":"2021-07-22T14:24:24.861941+00:00","investigations":[{"id":"SW52ZXN0aWdhdGlvbk5vZGU6NQ==","name":"Test Investigation 4","keywords":["Keyword 0","Keyword 1","Keyword 2","Keyword 3","Keyword 4"]}],"samples":[{"name":"Test Sample 5","id":"U2FtcGxlTm9kZTo1","url":"/media/uploads/simplified_sample_FsuBL5A.json","keywords":["Keyword 0","Keyword 1","Keyword 2","Keyword 3","Keyword 4"]}],"studies":[{"id":"U3R1ZHlOb2RlOjU=","name":"Test Study 4","investigations":[{"id":"SW52ZXN0aWdhdGlvbk5vZGU6NQ==","name":"Test Investigation 4","keywords":["Keyword 0","Keyword 1","Keyword 2","Keyword 3","Keyword 4"]}],"keywords":["Keyword 0","Keyword 1","Keyword 2","Keyword 3","Keyword 4"]}]}}]}}}
```
***
#### $ adc-user "<*user_id*>"

This command will return all the information linked to a specific user id. 
###### sample output:

```json
$ adc-user "VXNlck5vZGU6MQ=="
python main.py user VXNlck5vZGU6MQ==
This is your response:
{"data":{"user":{"id":"VXNlck5vZGU6MQ==","username":"gonzalo.martinez@domandtom.com","email":"gonzalo.martinez@domandtom.com","created":"2021-07-22T14:22:10.308545+00:00","updated":"2021-07-22T14:22:10.308568+00:00","investigations":[{"id":"SW52ZXN0aWdhdGlvbk5vZGU6Ng==","name":"Test Study Name","keywords":["test","graphql","demo","argonne"]},{"id":"SW52ZXN0aWdhdGlvbk5vZGU6Nw==","name":"Test Study Name","keywords":["test","graphql","demo","argonne"]}],"samples":[],"studies":[]}}}
```
***
#### $ adc-samples

This command will list all the samples currently available.
###### sample output:

```json
$ adc-samples
python main.py samples
This is your response:
{"data":{"samples":{"edges":[{"node":{"id":"U2FtcGxlTm9kZTox","name":"Test Sample 1","url":"/media/uploads/simplified_sample.json","keywords":["Keyword 0","Keyword 1","Keyword 2","Keyword 3","Keyword 4"],"created":"2021-07-22T14:24:24.872097+00:00","updated":"2021-07-22T14:24:24.880941+00:00","user":{"id":"VXNlck5vZGU6Mg==","username":"sherry38","email":"mayodeanna@williamson.com"},"isOwner":false}},{"node":{"id":"U2FtcGxlTm9kZTo1","name":"Test Sample 5","url":"/media/uploads/simplified_sample_FsuBL5A.json","keywords":["Keyword 0","Keyword 1","Keyword 2","Keyword 3","Keyword 4"],"created":"2021-07-22T14:24:24.896277+00:00","updated":"2021-07-22T14:24:24.897841+00:00","user":{"id":"VXNlck5vZGU6Ng==","username":"kentsanchez","email":"icabrera@gmail.com"},"isOwner":false}},{"node":{"id":"U2FtcGxlTm9kZToz","name":"Test Sample 3","url":"/media/uploads/simplified_sample_UYlPLPB.json","keywords":["Keyword 0","Keyword 1","Keyword 2","Keyword 3","Keyword 4"],"created":"2021-07-22T14:24:24.889214+00:00","updated":"2021-07-22T14:24:24.890941+00:00","user":{"id":"VXNlck5vZGU6NA==","username":"mmckay","email":"peggyspears@yahoo.com"},"isOwner":false}},{"node":{"id":"U2FtcGxlTm9kZTo0","name":"Test Sample 4","url":"/media/uploads/simplified_sample_qANM8An.json","keywords":["Keyword 0","Keyword 1","Keyword 2","Keyword 3","Keyword 4"],"created":"2021-07-22T14:24:24.892823+00:00","updated":"2021-07-22T14:24:24.894540+00:00","user":{"id":"VXNlck5vZGU6NQ==","username":"rfuller","email":"peterscristina@hotmail.com"},"isOwner":false}},{"node":{"id":"U2FtcGxlTm9kZToy","name":"Test Sample 2","url":"/media/uploads/simplified_sample_8JF3Ryx.json","keywords":["Keyword 0","Keyword 1","Keyword 2","Keyword 3","Keyword 4"],"created":"2021-07-22T14:24:24.885334+00:00","updated":"2021-07-22T14:24:24.887182+00:00","user":{"id":"VXNlck5vZGU6Mw==","username":"combsashlee","email":"carrillopatrick@hotmail.com"},"isOwner":false}}]}}}
```
***
#### $ adc-sample "<*sample_id*>"

This command will return all the information linked to the specified sample id.
###### sample output:

```json
$ adc-sample "U2FtcGxlTm9kZTox"
python main.py sample U2FtcGxlTm9kZTox
This is your response:
{"data":{"sample":{"id":"U2FtcGxlTm9kZTox","name":"Test Sample 1","keywords":["Keyword 0","Keyword 1","Keyword 2","Keyword 3","Keyword 4"],"url":"/media/uploads/simplified_sample.json","created":"2021-07-22T14:24:24.872097+00:00","updated":"2021-07-22T14:24:24.880941+00:00","user":{"id":"VXNlck5vZGU6Mg==","username":"sherry38","email":"mayodeanna@williamson.com"},"isOwner":false}}}
```
***
#### $ adc-createsample 

This command will help you to create a new sample.
###### sample output:

```json
$ adc-createsample
python main.py createsample
Enter operation
{"query":"mutation ($name: String!, $parentId: ID, $keywords: [String!], $file: Upload!) {createSample(name: $name, parentId: $parentId, keywords: $keywords, file: $file) {sample { id name keywords url}}}",     "variables": { "name": "test sample", "keywords": ["test", "python"], "file": null}}
Enter map
{ "0": ["variables.file"]}
enter file
sample.json
This is your response:
{"data":{"createSample":{"sample":{"id":"U2FtcGxlTm9kZToyOQ==","name":"test sample","keywords":["python","test"],"url":"/media/uploads/sample_Eb7D9hi.json"}}}}
```


***
#### $ adc-studies

This command will list all the available studies.
###### sample output:

```json
$  adc-studies
python main.py studies
This is your response:
{"data":{"studies":{"edges":[{"node":{"id":"U3R1ZHlOb2RlOjE=","name":"Test Study 0","description":"Offer concern notice state me knowledge. Drug same man door skin. Region drive clearly American crime argue who.\nAnd must idea building carry.\nWestern teacher hard this assume father professor.","created":"2021-07-22T14:24:24.828652+00:00","updated":"2021-07-22T14:24:24.828665+00:00","keywords":["Keyword 0","Keyword 1","Keyword 2","Keyword 3","Keyword 4"],"investigations":[{"id":"SW52ZXN0aWdhdGlvbk5vZGU6MQ==","name":"Test Investigation 0","samples":[{"id":"U2FtcGxlTm9kZTox","name":"Test Sample 1","url":"/media/uploads/simplified_sample.json"}]},{"id":"SW52ZXN0aWdhdGlvbk5vZGU6Ng==","name":"Test Study Name","samples":[]},{"id":"SW52ZXN0aWdhdGlvbk5vZGU6Nw==","name":"Test Study Name","samples":[{"id":"U2FtcGxlTm9kZToy","name":"Test Sample 2","url":"/media/uploads/simplified_sample_8JF3Ryx.json"}]}],"user":{"id":"VXNlck5vZGU6Mg==","username":"sherry38","email":"mayodeanna@williamson.com"},"isOwner":false}},{"node":{"id":"U3R1ZHlOb2RlOjI=","name":"Test Study 1","description":"Drop defense star hospital raise recently. Policy possible degree often.\nWell us game Democrat.\nDetermine security music deal ball. Notice traditional allow protect country care glass.","created":"2021-07-22T14:24:24.844341+00:00","updated":"2021-07-22T14:24:24.844351+00:00","keywords":["Keyword 0","Keyword 1","Keyword 2","Keyword 3","Keyword 4"],"investigations":[{"id":"SW52ZXN0aWdhdGlvbk5vZGU6Mg==","name":"Test Investigation 1","samples":[{"id":"U2FtcGxlTm9kZToy","name":"Test Sample 2","url":"/media/uploads/simplified_sample_8JF3Ryx.json"}]}],"user":{"id":"VXNlck5vZGU6Mw==","username":"combsashlee","email":"carrillopatrick@hotmail.com"},"isOwner":false}},{"node":{"id":"U3R1ZHlOb2RlOjM=","name":"Test Study 2","description":"Threat collection management skill general. Security statement range.\nEdge security water choice determine save fire simply. Campaign drug pass subject. Yes expect campaign his end this.","created":"2021-07-22T14:24:24.851772+00:00","updated":"2021-07-22T14:24:24.851779+00:00","keywords":["Keyword 0","Keyword 1","Keyword 2","Keyword 3","Keyword 4"],"investigations":[{"id":"SW52ZXN0aWdhdGlvbk5vZGU6Mw==","name":"Test Investigation 2","samples":[{"id":"U2FtcGxlTm9kZToz","name":"Test Sample 3","url":"/media/uploads/simplified_sample_UYlPLPB.json"}]}],"user":{"id":"VXNlck5vZGU6NA==","username":"mmckay","email":"peggyspears@yahoo.com"},"isOwner":false}},{"node":{"id":"U3R1ZHlOb2RlOjQ=","name":"Test Study 3","description":"Wind purpose in product himself collection say. Language somebody fill future. Impact tree model.","created":"2021-07-22T14:24:24.857936+00:00","updated":"2021-07-22T14:24:24.857943+00:00","keywords":["Keyword 0","Keyword 1","Keyword 2","Keyword 3","Keyword 4"],"investigations":[{"id":"SW52ZXN0aWdhdGlvbk5vZGU6NA==","name":"Test Investigation 3","samples":[{"id":"U2FtcGxlTm9kZTo0","name":"Test Sample 4","url":"/media/uploads/simplified_sample_qANM8An.json"}]}],"user":{"id":"VXNlck5vZGU6NQ==","username":"rfuller","email":"peterscristina@hotmail.com"},"isOwner":false}},{"node":{"id":"U3R1ZHlOb2RlOjU=","name":"Test Study 4","description":"Plant window education inside test. Spring know figure certainly want development brother.\nCouple throw fish suddenly. Individual kitchen factor develop network institution.","created":"2021-07-22T14:24:24.862793+00:00","updated":"2021-07-22T14:24:24.862799+00:00","keywords":["Keyword 0","Keyword 1","Keyword 2","Keyword 3","Keyword 4"],"investigations":[{"id":"SW52ZXN0aWdhdGlvbk5vZGU6NQ==","name":"Test Investigation 4","samples":[{"id":"U2FtcGxlTm9kZTo1","name":"Test Sample 5","url":"/media/uploads/simplified_sample_FsuBL5A.json"}]}],"user":{"id":"VXNlck5vZGU6Ng==","username":"kentsanchez","email":"icabrera@gmail.com"},"isOwner":false}}]}}}
```
***
#### $ adc-study "<*study_id*>"

This command will return all the information linked to a specific study id.
###### sample output:

```json
$  adc-study "U3R1ZHlOb2RlOjE="
python main.py study U3R1ZHlOb2RlOjE=
This is your response:
{"data":{"study":{"id":"U3R1ZHlOb2RlOjE=","name":"Test Study 0","description":"Offer concern notice state me knowledge. Drug same man door skin. Region drive clearly American crime argue who.\nAnd must idea building carry.\nWestern teacher hard this assume father professor.","created":"2021-07-22T14:24:24.828652+00:00","updated":"2021-07-22T14:24:24.828665+00:00","keywords":["Keyword 0","Keyword 1","Keyword 2","Keyword 3","Keyword 4"],"investigations":[{"id":"SW52ZXN0aWdhdGlvbk5vZGU6MQ==","name":"Test Investigation 0","samples":[{"id":"U2FtcGxlTm9kZTox","name":"Test Sample 1","url":"/media/uploads/simplified_sample.json"}]},{"id":"SW52ZXN0aWdhdGlvbk5vZGU6Ng==","name":"Test Study Name","samples":[]},{"id":"SW52ZXN0aWdhdGlvbk5vZGU6Nw==","name":"Test Study Name","samples":[{"id":"U2FtcGxlTm9kZToy","name":"Test Sample 2","url":"/media/uploads/simplified_sample_8JF3Ryx.json"}]}],"user":{"id":"VXNlck5vZGU6Mg==","username":"sherry38","email":"mayodeanna@williamson.com"},"isOwner":false}}}
```
***

#### $ adc-createstudy "<*file.json*>"

This command will create a study from a json file.\
This *file.json* must exist in the **variables** folder prior to executing the command. \
You can create a new *file.json* within the **variables** folder by issuing the following command: \
```
adc-createvariables
```

###### sample output:

```json
$  adc-createstudy '{"name": "Test Study Name", "description": "Test Study Description", "keywords": ["test", "graphql", "demo", "argonne"]}'
   python main.py createstudy createStudy.json
This is your response:
{"data":{"createStudy":{"study":{"id":"U3R1ZHlOb2RlOjY=","name":"Test Study Name","description":"Test Study Description","keywords":["test","graphql","demo","argonne"],"isOwner":true,"user":{"id":"VXNlck5vZGU6MQ==","username":"gonzalo.martinez@domandtom.com"},"investigations":[]}}}}

```
***
#### $ adc-investigations

This command will return a list containing all the available investigations 
###### sample output:

```json
$ adc-investigations
python main.py investigations
This is your response:
{"data":{"investigations":{"edges":[{"node":{"id":"SW52ZXN0aWdhdGlvbk5vZGU6MQ==","name":"Test Investigation 0","description":"Indeed it enter size. If table stuff bill dark happy majority. Cell north on north.","keywords":["Keyword 0","Keyword 1","Keyword 2","Keyword 3","Keyword 4"],"created":"2021-07-22T14:24:24.836075+00:00","updated":"2021-07-22T14:24:24.836084+00:00","study":{"id":"U3R1ZHlOb2RlOjE=","name":"Test Study 0","description":"Offer concern notice state me knowledge. Drug same man door skin. Region drive clearly American crime argue who.\nAnd must idea building carry.\nWestern teacher hard this assume father professor.","keywords":["Keyword 0","Keyword 1","Keyword 2","Keyword 3","Keyword 4"]},"user":{"id":"VXNlck5vZGU6Mg==","username":"sherry38","email":"mayodeanna@williamson.com"},"samples":[{"id":"U2FtcGxlTm9kZTox","name":"Test Sample 1","url":"/media/uploads/simplified_sample.json"}],"isOwner":false}},{"node":{"id":"SW52ZXN0aWdhdGlvbk5vZGU6Mg==","name":"Test Investigation 1","description":"Benefit his it. Remain drop base its. Usually environmental ability team worker.\nFamily indicate research. Film behind art fish travel you without. Population drug machine tough president.","keywords":["Keyword 0","Keyword 1","Keyword 2","Keyword 3","Keyword 4"],"created":"2021-07-22T14:24:24.847524+00:00","updated":"2021-07-22T14:24:24.847533+00:00","study":{"id":"U3R1ZHlOb2RlOjI=","name":"Test Study 1","description":"Drop defense star hospital raise recently. Policy possible degree often.\nWell us game Democrat.\nDetermine security music deal ball. Notice traditional allow protect country care glass.","keywords":["Keyword 0","Keyword 1","Keyword 2","Keyword 3","Keyword 4"]},"user":{"id":"VXNlck5vZGU6Mw==","username":"combsashlee","email":"carrillopatrick@hotmail.com"},"samples":[{"id":"U2FtcGxlTm9kZToy","name":"Test Sample 2","url":"/media/uploads/simplified_sample_8JF3Ryx.json"}],"isOwner":false}},{"node":{"id":"SW52ZXN0aWdhdGlvbk5vZGU6Mw==","name":"Test Investigation 2","description":"Level power song parent its buy small. Society agreement though. Then whose build class debate significant.","keywords":["Keyword 0","Keyword 1","Keyword 2","Keyword 3","Keyword 4"],"created":"2021-07-22T14:24:24.854446+00:00","updated":"2021-07-22T14:24:24.854453+00:00","study":{"id":"U3R1ZHlOb2RlOjM=","name":"Test Study 2","description":"Threat collection management skill general. Security statement range.\nEdge security water choice determine save fire simply. Campaign drug pass subject. Yes expect campaign his end this.","keywords":["Keyword 0","Keyword 1","Keyword 2","Keyword 3","Keyword 4"]},"user":{"id":"VXNlck5vZGU6NA==","username":"mmckay","email":"peggyspears@yahoo.com"},"samples":[{"id":"U2FtcGxlTm9kZToz","name":"Test Sample 3","url":"/media/uploads/simplified_sample_UYlPLPB.json"}],"isOwner":false}},{"node":{"id":"SW52ZXN0aWdhdGlvbk5vZGU6NA==","name":"Test Investigation 3","description":"Catch ahead such something town wonder address. Pm thank that recognize. Window these against decade part player mission.","keywords":["Keyword 0","Keyword 1","Keyword 2","Keyword 3","Keyword 4"],"created":"2021-07-22T14:24:24.859853+00:00","updated":"2021-07-22T14:24:24.859859+00:00","study":{"id":"U3R1ZHlOb2RlOjQ=","name":"Test Study 3","description":"Wind purpose in product himself collection say. Language somebody fill future. Impact tree model.","keywords":["Keyword 0","Keyword 1","Keyword 2","Keyword 3","Keyword 4"]},"user":{"id":"VXNlck5vZGU6NQ==","username":"rfuller","email":"peterscristina@hotmail.com"},"samples":[{"id":"U2FtcGxlTm9kZTo0","name":"Test Sample 4","url":"/media/uploads/simplified_sample_qANM8An.json"}],"isOwner":false}},{"node":{"id":"SW52ZXN0aWdhdGlvbk5vZGU6NQ==","name":"Test Investigation 4","description":"Maybe professor beyond than. Pay important home.\nWhen approach shoulder. Media allow state attorney. Physical product enter professional hot station dream.","keywords":["Keyword 0","Keyword 1","Keyword 2","Keyword 3","Keyword 4"],"created":"2021-07-22T14:24:24.864781+00:00","updated":"2021-07-22T14:24:24.864786+00:00","study":{"id":"U3R1ZHlOb2RlOjU=","name":"Test Study 4","description":"Plant window education inside test. Spring know figure certainly want development brother.\nCouple throw fish suddenly. Individual kitchen factor develop network institution.","keywords":["Keyword 0","Keyword 1","Keyword 2","Keyword 3","Keyword 4"]},"user":{"id":"VXNlck5vZGU6Ng==","username":"kentsanchez","email":"icabrera@gmail.com"},"samples":[{"id":"U2FtcGxlTm9kZTo1","name":"Test Sample 5","url":"/media/uploads/simplified_sample_FsuBL5A.json"}],"isOwner":false}},{"node":{"id":"SW52ZXN0aWdhdGlvbk5vZGU6Ng==","name":"Test Study Name","description":"Test Study Description","keywords":["test","graphql","demo","argonne"],"created":"2021-07-22T14:25:02.619215+00:00","updated":"2021-07-22T14:25:02.619226+00:00","study":{"id":"U3R1ZHlOb2RlOjE=","name":"Test Study 0","description":"Offer concern notice state me knowledge. Drug same man door skin. Region drive clearly American crime argue who.\nAnd must idea building carry.\nWestern teacher hard this assume father professor.","keywords":["Keyword 0","Keyword 1","Keyword 2","Keyword 3","Keyword 4"]},"user":{"id":"VXNlck5vZGU6MQ==","username":"gonzalo.martinez@domandtom.com","email":"gonzalo.martinez@domandtom.com"},"samples":[],"isOwner":true}},{"node":{"id":"SW52ZXN0aWdhdGlvbk5vZGU6Nw==","name":"Test Study Name","description":"Test Study Description","keywords":["test","graphql","demo","argonne"],"created":"2021-07-22T14:26:07.152748+00:00","updated":"2021-07-22T14:26:07.152769+00:00","study":{"id":"U3R1ZHlOb2RlOjE=","name":"Test Study 0","description":"Offer concern notice state me knowledge. Drug same man door skin. Region drive clearly American crime argue who.\nAnd must idea building carry.\nWestern teacher hard this assume father professor.","keywords":["Keyword 0","Keyword 1","Keyword 2","Keyword 3","Keyword 4"]},"user":{"id":"VXNlck5vZGU6MQ==","username":"gonzalo.martinez@domandtom.com","email":"gonzalo.martinez@domandtom.com"},"samples":[{"id":"U2FtcGxlTm9kZToy","name":"Test Sample 2","url":"/media/uploads/simplified_sample_8JF3Ryx.json"}],"isOwner":true}}]}}}
```
***
#### $ adc-inv <*investigation_node_id*>

This command  will return a list of all available investigations linked to that investigation_node_id.
###### sample output:

```json
$ adc-inv "SW52ZXN0aWdhdGlvbk5vZGU6MQ=="
python main.py investigation SW52ZXN0aWdhdGlvbk5vZGU6MQ==
This is your response:
{"data":{"investigation":{"id":"SW52ZXN0aWdhdGlvbk5vZGU6MQ==","name":"Test Investigation 0","description":"Indeed it enter size. If table stuff bill dark happy majority. Cell north on north.","keywords":["Keyword 0","Keyword 1","Keyword 2","Keyword 3","Keyword 4"],"created":"2021-07-22T14:24:24.836075+00:00","updated":"2021-07-22T14:24:24.836084+00:00","study":{"id":"U3R1ZHlOb2RlOjE=","name":"Test Study 0","description":"Offer concern notice state me knowledge. Drug same man door skin. Region drive clearly American crime argue who.\nAnd must idea building carry.\nWestern teacher hard this assume father professor.","keywords":["Keyword 0","Keyword 1","Keyword 2","Keyword 3","Keyword 4"]},"user":{"id":"VXNlck5vZGU6Mg==","username":"sherry38","email":"mayodeanna@williamson.com"},"samples":[{"id":"U2FtcGxlTm9kZTox","name":"Test Sample 1","url":"/media/uploads/simplified_sample.json"}],"isOwner":false}}}
```

***

#### $ adc-create-inv '{"name": "Test Study Name", "description": "Test Study Description", "keywords": ["test", "graphql", "demo", "argonne"], "sampleGlobalIds" : ["VXNlck5vZGU6Mg=="], "studyGlobalId": "U3R1ZHlOb2RlOjE="}'

This command will create a new investigation from a json file.\

###### sample output:

```json
$ adc-createinvestigation
python main.py createinvestigation createInvestigation.json
This is your response:
{"data":{"createInvestigation":{"investigation":{"id":"SW52ZXN0aWdhdGlvbk5vZGU6OA==","name":"Test Study Name","description":"Test Study Description","isOwner":true,"keywords":["test","graphql","demo","argonne"],"study":{"id":"U3R1ZHlOb2RlOjE=","name":"Test Study 0"},"samples":[{"id":"U2FtcGxlTm9kZToy"}],"user":{"id":"VXNlck5vZGU6MQ==","username":"gonzalo.martinez@domandtom.com"}}}}}
```
***