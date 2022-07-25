import io
from urllib.parse import urlencode

from .bp import bp

from flask import (url_for, flash, render_template,
        redirect, session, send_file, jsonify, abort)
from flask import ( request as req,
        make_response as mkrsp,
        Response as Rsp,
        )

from .._imdata import ImData

@bp.route('/')
def index():
    message = req.args.get("message", None)
    return render_template('imdata/index.html', message = message)

@bp.route('/handle', methods = ["GET", "POST"])
def handle():
    operation = req.values.get("operation")

    method = req.values.get("method")

    data = req.files.get("file")
    if not data:
        data = req.values.get("ctx", req.values.get("file", None))
    else:
        data = data.read()

    # print("data:", data)
    print("method:", method)
    print(req.files, req.values, req.values.keys(), sep='\n\n')

    if operation == 'decode':
        imdata = ImData()
        imdata.read(imdata.to_bytes(data))

        urlbase = "/imdata/download?"
        params = urlencode({"file" : imdata.content})

        try:
            origin = imdata.to_string(imdata.content)
            use_file = False
        except:
            origin = imdata.content
            use_file = True

        return render_template("imdata/origin.html", origin = origin, use_file = use_file, url = urlbase + params)

    if not data:
        return redirect(url_for(".index") + "?message=没有内容输入！")
    if method == '1':
        # 压缩数据
        ctt = io.BytesIO()
        ImData(data).save(ctt)
        # must, or can't send
        ctt.seek(0)
        # send_file(filename_or_fp, mimetype=None, as_attachment=False, attachment_filename=None, add_etags=True, cache_timeout=None, conditional=False)
        return send_file(ctt, "image/bmp", True, "data.bmp")
    elif method == '2':
        # Chencode集成
        return redirect(url_for('.index') + "?message=暂不支持ChEncode集成")
    else:
        # 错误方法
        abort(400)
    return "Fuck you"

@bp.route('/download')
def download():
    file = io.BytesIO(req.values.get("file").encode())
    file.seek(0)
    # print(req.files, req.values, req.values.keys(), sep='\n')
    return send_file(file, "plain/text", True, "data.txt")

@bp.route('/encode', methods=["GET", "POST"])
def encode():
    # test with command
    # curl 127.0.0.1:5000/imdata/encode --data ctx="something here" -o data.bmp
    # curl 127.0.0.1:5000/imdata/encode --form file=@filename -o data.bmp

    file = req.files.get("file")
    print(req.files, req.values, req.values.keys(),sep='\n\n')
    if not file:
        file = req.values.get("ctx", req.values.get("file", None))
    else:
        file = file.read()

    if not file:
        abort(404)


    ctx = io.BytesIO()
    ImData().save(ctx, file)
    ctx.seek(0)

    # send_file(path_or_file: Union[os.PathLike, str, BinaryIO], mimetype: Optional[str] = None, as_attachment: bool = False, download_name: Optional[str] = None, attachment_filename: Optional[str] = None, conditional: bool = True, etag: Union[bool, str] = True, add_etags: Optional[bool] = None, last_modified: Union[datetime.datetime, int, float, NoneType] = None, max_age: Union[int, Callable[[Optional[str]], Optional[int]], NoneType] = None, cache_timeout: Optional[int] = None)

    return send_file(ctx, "image/bmp", True, "data.bmp", "data.bmp")

@bp.route('/decode', methods=["GET", "POST"])
def decode():
    # test with
    # curl 127.0.0.1:5000/imdata/encode --form file=@data.bmp
    # better use post method, not get!

    file = req.files.get("file", None)
    if not file:
        file = req.values.get("ctx", req.values.get("file", None))
    else:
        file = file.read()

    if not file:
        abort(404)

    file = ImData.to_bytes(file)

    return ImData().read(file)
