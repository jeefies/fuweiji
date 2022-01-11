from .bp import bp

from flask import (url_for, flash, render_template,
        redirect, session, send_file, jsonify, abort)
from flask import ( request as req,
        make_response as mkrsp,
        Response as Rsp,
        )

import io

from .._imdata import ImData

@bp.route('/')
def index():
    return render_template('imdata/index.html')

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
