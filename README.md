local test
docker build -t stevneevilimage .

docker run -d --name mycontainer -p 80:80 stevneevilimage

curl -XPOST localhost/bad
curl -XPOST localhost/bad
{"hashes":{"sha256":"7bc9f3ad33b53e51a044099a2cc8cff83e9193eaf099c4f2412e84da103c4910","md5":"d07b3fde2ac09f906346fc9c17b8cbe9"}}stevepro@Tigera:~/Steven/Python/DockerEvil$

{"hashes":{"md5":"d07b3fde2ac09f906346fc9c17b8cbe9","sha1":"2d91c49ecc4878ea4b261e239208f12c7be36bcd","sha256":"7bc9f3ad33b53e51a044099a2cc8cff83e9193eaf099c4f2412e84da103c4910"}}


{
    "md5": "d07b3fde2ac09f906346fc9c17b8cbe9",
    "sha1": "2d91c49ecc4878ea4b261e239208f12c7be36bcd",
    "sha256": "7bc9f3ad33b53e51a044099a2cc8cff83e9193eaf099c4f2412e84da103c4910"
}

curl http://127.0.0.1/items/7?q=stevepro






docker tag stevneevilimage:latest steventigera/stevneevilimage
docker push steventigera/stevneevilimage


kubectl run stevenevil --image steventigera/myimage

kubectl exec -it stevenevil -- curl localhost/items/7?q=stevepro