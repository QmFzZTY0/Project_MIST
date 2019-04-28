import requests

headers={
'User-Agent':'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/61.0.3163.100 Safari/537.36',
'Referer':'https://steamcn.com/member.php?mod=logging&action=login',
'Cookie':'__cfduid=d649561d2c0ac7c19848c46030a844e031546067663; yjs_id=e11d7802a73a9f02d481f0abd64bd823; _ga=GA1.2.1930950146.1546067670; ctrl_time=1; _gid=GA1.2.424111747.1548413932; __51cke__=; Hm_lvt_6f8cbab9ce04cc0b22fe567594c76fff=1548149131,1548413932,1548450529,1548450699; dz_2132_sid=fLr9oA; dz_2132_saltkey=Xs9uz3Z8; dz_2132_lastvisit=1548447121; dz_2132_sendmail=1; dz_2132_ulastactivity=e56a6sntfTPacwg612cNZ3bI1wDJZxUTES2lgmnTJL6Q5voqegBF; dz_2132_auth=8b89vaSPxfZjGr59mqsIJtueoGKEskfYbuIbjHrBn2eI7U2BB1ZeGR9OLC9Gy5hABnmY2uiP71OUBGAN%2Fp0Ed0JwjQA; dz_2132_lastcheckfeed=242859%7C1548450733; dz_2132_checkfollow=1; dz_2132_lip=112.10.95.193%2C1548450713; dz_2132_connect_is_bind=0; dz_2132_nofavfid=1; dz_2132_checkpm=1; __tins__880528=%7B%22sid%22%3A%201548450698955%2C%20%22vd%22%3A%207%2C%20%22expires%22%3A%201548452536557%7D; __51laig__=7; Hm_lpvt_6f8cbab9ce04cc0b22fe567594c76fff=1548450737; dz_2132_lastact=1548450736%09misc.php%09patch'
}

res=requests.get("https://steamcn.com/",headers=headers)

