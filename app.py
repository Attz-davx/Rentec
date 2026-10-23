from flask import Flask, render_template, request, session, redirect, url_for, send_file
from flask_mysqldb import MySQL
from flask import render_template, request, redirect, url_for, session
from werkzeug.security import generate_password_hash, check_password_hash
from datetime import timedelta

from openpyxl import Workbook
import io


app = Flask(__name__)


# =========================================================
# CONFIGURACIÓN DE SESIÓN
# =========================================================

app.secret_key = "rentec_clave_segura"

# La sesión permanecerá activa durante 7 días
app.permanent_session_lifetime = timedelta(days=7)


# ==========================================
# Configuración MySQL para bd local
# ==========================================

# app.config["MYSQL_HOST"] = "localhost"
# app.config["MYSQL_USER"] = "root"
# app.config["MYSQL_PASSWORD"] = ""
# app.config["MYSQL_DB"] = "rentec"

# mysql = MySQL(app)


# ==========================================
# Configuración MySQL para bd en aiven
# ==========================================

app.config['MYSQL_HOST'] = os.environ.get('MYSQL_HOST')
app.config['MYSQL_USER'] = os.environ.get('MYSQL_USER')
app.config['MYSQL_PASSWORD'] = os.environ.get('MYSQL_PASSWORD')
app.config['MYSQL_DB'] = os.environ.get('MYSQL_DB')
app.config['MYSQL_PORT'] = int(os.environ.get('MYSQL_PORT', 3306))

mysql = MySQL(app)


# =========================================================
# PÁGINA PRINCIPAL
# =========================================================

@app.route("/")
def inicio():

    return render_template(
        "index.html",
        nombre=session.get("nombre"),
        rol=session.get("rol")
    )


# =========================================================
# CATÁLOGO
# =========================================================

@app.route("/computadores")
def computadores():

    return render_template("computadores.html")


# =========================================================
# detalles de los computadores 
# =========================================================

@app.route("/computador1")
def computador1():

    return render_template("computador1.html")


@app.route("/computador2")
def computador2():

    return render_template("computador2.html")


@app.route("/computador3")
def computador3():

    return render_template("computador3.html")


@app.route("/computador4")
def computador4():

    return render_template("computador4.html")


@app.route("/computador5")
def computador5():

    return render_template("computador5.html")


@app.route("/computador6")
def computador6():

    return render_template("computador6.html")


@app.route("/computador7")
def computador7():

    return render_template("computador7.html")


@app.route("/computador8")
def computador8():

    return render_template("computador8.html")


@app.route("/computador9")
def computador9():

    return render_template("computador9.html")



@app.route("/carrito")
def carrito():
    productos_carrito = session.get("carrito", [])
    total = 0

    for producto in productos_carrito:
        tarifa = (
            producto["precio_dia"]
            if producto["duracion"] == "dia"
            else producto["precio_hora"]
        )

        producto["subtotal"] = (
            tarifa * producto["tiempo"] * producto["cantidad"]
        )
        total += producto["subtotal"]

    return render_template(
        "carrito.html",
        carrito=productos_carrito,
        total=total
    )



@app.route("/computador10")
def computador10():

    return render_template("computador10.html")  

@app.route("/computador11")
def computador11():

    return render_template("computador11.html")

@app.route("/computador12")
def computador12():

    return render_template("computador12.html")  

@app.route("/computador13")
def computador13():

    return render_template("computador13.html")

@app.route("/computador14")
def computador14():

    return render_template("computador14.html")

@app.route("/computador15")
def computador15():

    return render_template("computador15.html")    

@app.route("/computador16")
def computador16():

    return render_template("computador16.html")

@app.route("/computador17")
def computador17():

    return render_template("computador17.html")

@app.route("/computador18")
def computador18():

    return render_template("computador18.html")
    
@app.route("/tecladosmaus")
def tecladosmaus():

    return render_template("tecladosmaus.html")

# Detalles de teclados
@app.route("/teclado1")
def teclado1():
    return render_template("teclado1.html")

@app.route("/teclado2")
def teclado2():
    return render_template("teclado2.html")

@app.route("/teclado3")
def teclado3():
    return render_template("teclado3.html")

@app.route("/teclado4")
def teclado4():
    return render_template("teclado4.html")


# Detalles de mouse
@app.route("/mouse1")
def mouse1():
    return render_template("mouse1.html")

@app.route("/mouse2")
def mouse2():
    return render_template("mouse2.html")

@app.route("/mouse3")
def mouse3():
    return render_template("mouse3.html")

@app.route("/mouse4")
def mouse4():
    return render_template("mouse4.html")

@app.route("/mouse5")
def mouse5():
    return render_template("mouse5.html")


@app.route("/televisores")
def televisores():

    return render_template("televisores.html")


@app.route("/televisor1")
def televisor1():
    return render_template("televisor1.html")


@app.route("/televisor2")
def televisor2():
    return render_template("televisor2.html")


@app.route("/televisor3")
def televisor3():
    return render_template("televisor3.html")


@app.route("/televisor4")
def televisor4():
    return render_template("televisor4.html")


@app.route("/televisor5")
def televisor5():
    return render_template("televisor5.html")


@app.route("/televisor6")
def televisor6():
    return render_template("televisor6.html")


@app.route("/televisor7")
def televisor7():
    return render_template("televisor7.html")


@app.route("/televisor8")
def televisor8():
    return render_template("televisor8.html")


@app.route("/televisor9")
def televisor9():
    return render_template("televisor9.html")



@app.route("/torresdepc")
def torresdepc():

    return render_template("torresdepc.html")

# DETALLES DE LAS TORRES DE PC

@app.route("/torre1")
def torre1():
    return render_template("torre1.html")

@app.route("/torre2")
def torre2():
    return render_template("torre2.html")

@app.route("/torre3")
def torre3():
    return render_template("torre3.html")

@app.route("/torre4")
def torre4():
    return render_template("torre4.html")

@app.route("/torre5")
def torre5():
    return render_template("torre5.html")

@app.route("/torre6")
def torre6():
    return render_template("torre6.html")

@app.route("/torre7")
def torre7():
    return render_template("torre7.html")

@app.route("/torre8")
def torre8():
    return render_template("torre8.html")

@app.route("/torre9")
def torre9():
    return render_template("torre9.html")


# =========================================================
# NOSOTROS
# =========================================================

@app.route("/nosotros")
def nosotros():

    return render_template("quienesomos.html")


@app.route("/mision")
def mision():

    return render_template("misionyvision.html")


# =========================================================
# LOGIN Y REGISTRO
# =========================================================

@app.route("/login-registro")
def login_registro():

    return render_template("Login-Registro.html")


# =========================================================
# REGISTRO
# =========================================================

@app.route("/registro", methods=["GET", "POST"])
def registro():

    if request.method == "POST":

        # -------------------------------------------------
        # DATOS DEL FORMULARIO
        # -------------------------------------------------

        nombre = request.form["nombre"]
        correo = request.form["correo"]
        telefono = request.form["telefono"]
        usuario = request.form["usuario"]
        password = request.form["password"]

        # -------------------------------------------------
        # ENCRIPTAR CONTRASEÑA
        # -------------------------------------------------

        password_hash = generate_password_hash(password)

        cursor = mysql.connection.cursor()


        # -------------------------------------------------
        # COMPROBAR USUARIO
        # -------------------------------------------------

        cursor.execute(
            "SELECT id FROM usuarios WHERE usuario = %s",
            (usuario,)
        )

        existe = cursor.fetchone()

        if existe:

            cursor.close()

            return """
            <script>
                alert("El nombre de usuario ya existe");
                window.location.href="/registro";
            </script>
            """


        # -------------------------------------------------
        # COMPROBAR CORREO
        # -------------------------------------------------

        cursor.execute(
            "SELECT id FROM usuarios WHERE correo = %s",
            (correo,)
        )

        correo_existe = cursor.fetchone()

        if correo_existe:

            cursor.close()

            return """
            <script>
                alert("El correo electrónico ya está registrado");
                window.location.href="/registro";
            </script>
            """


        # -------------------------------------------------
        # INSERTAR USUARIO
        # -------------------------------------------------
        #
        # ID DE ROLES:
        #
        # 1 = Administrador
        # 2 = Cliente
        #
        # Los usuarios que se registren normalmente
        # serán clientes.
        # -------------------------------------------------

        cursor.execute("""
            INSERT INTO usuarios
            (
                nombre_completo,
                correo,
                telefono,
                usuario,
                contrasena,
                id_rol
            )
            VALUES (%s, %s, %s, %s, %s, %s)
        """, (
            nombre,
            correo,
            telefono,
            usuario,
            password_hash,
            2
        ))

        mysql.connection.commit()

        cursor.close()

        return render_template("registro_exitoso.html")


    return render_template("Registro.html")


# =========================================================
# LOGIN
# =========================================================

@app.route("/login", methods=["GET", "POST"])
def login():

    if request.method == "POST":

        usuario = request.form["usuario"]
        password = request.form["password"]


        # -------------------------------------------------
        # BUSCAR USUARIO
        # -------------------------------------------------

        cursor = mysql.connection.cursor()

        # Obtenemos el nombre del rol mediante JOIN
        cursor.execute("""
            SELECT
                usuarios.id,
                usuarios.nombre_completo,
                usuarios.contrasena,
                roles.rol
            FROM usuarios
            INNER JOIN roles
                ON usuarios.id_rol = roles.id_rol
            WHERE usuarios.usuario = %s
        """, (usuario,))

        usuario_db = cursor.fetchone()

        cursor.close()


        # -------------------------------------------------
        # USUARIO NO EXISTE
        # -------------------------------------------------

        if usuario_db is None:

            return """
            <script>
                alert("El usuario no existe");
                window.location.href="/login";
            </script>
            """


        # -------------------------------------------------
        # OBTENER DATOS
        # -------------------------------------------------

        id_usuario = usuario_db[0]
        nombre = usuario_db[1]
        password_hash = usuario_db[2]
        rol = usuario_db[3]


        # -------------------------------------------------
        # COMPROBAR CONTRASEÑA
        # -------------------------------------------------

        if not check_password_hash(password_hash, password):

            return """
            <script>
                alert("Contraseña incorrecta");
                window.location.href="/login";
            </script>
            """


        # -------------------------------------------------
        # CREAR SESIÓN
        # -------------------------------------------------

        session.permanent = True

        session["id_usuario"] = id_usuario
        session["nombre"] = nombre
        session["rol"] = rol


        # -------------------------------------------------
        # MOSTRAR MENSAJE
        # -------------------------------------------------

        return redirect(url_for("inicio_exitoso"))


    return render_template("Login.html")


# =========================================================
# MENSAJE DE LOGIN EXITOSO
# =========================================================

@app.route("/inicio_exitoso")
def inicio_exitoso():

    # Si no hay sesión, no puede entrar
    if "id_usuario" not in session:

        return redirect(url_for("login"))


    return render_template(
        "login_exitoso.html"
    )


# =========================================================
# INICIO DEL USUARIO
# =========================================================

@app.route("/inicio_usuario")
def inicio_usuario():

    # Verificar que haya iniciado sesión
    if "id_usuario" not in session:

        return redirect(url_for("login"))


    return render_template(
        "inicio_usuario.html",
        nombre=session["nombre"],
        rol=session.get("rol")
    )


# =========================================================
# PANEL DE ADMINISTRADOR
# =========================================================

@app.route("/administrador")
def administrador():

    # Verificar sesión
    if "id_usuario" not in session:

        return redirect(url_for("login"))


    # Verificar administrador
    if session.get("rol") != "Administrador":

        return redirect(url_for("inicio_usuario"))


    return render_template(
        "administrador.html",
        nombre=session["nombre"]
    )


# =========================================================
# GESTIÓN DE USUARIOS
# =========================================================

@app.route("/administrador/usuarios", methods=["GET", "POST"])
def gestionar_usuarios():

    # Verificar sesión
    if "id_usuario" not in session:
        return redirect(url_for("login"))

    # Solo administrador
    if session.get("rol") != "Administrador":
        return redirect(url_for("inicio_usuario"))

    cursor = mysql.connection.cursor()

    # =====================================================
    # MODIFICAR USUARIO
    # =====================================================

    if request.method == "POST":

        id_usuario = request.form["id_usuario"]
        nombre = request.form["nombre"]
        correo = request.form["correo"]
        telefono = request.form["telefono"]
        usuario = request.form["usuario"]
        id_rol = request.form["id_rol"]

        cursor.execute("""
            UPDATE usuarios
            SET
                nombre_completo = %s,
                correo = %s,
                telefono = %s,
                usuario = %s,
                id_rol = %s
            WHERE id = %s
        """, (
            nombre,
            correo,
            telefono,
            usuario,
            id_rol,
            id_usuario
        ))

        mysql.connection.commit()
        cursor.close()

        return redirect(url_for("gestionar_usuarios"))

    # =====================================================
    # OBTENER USUARIOS
    # =====================================================

    cursor.execute("""
        SELECT
            usuarios.id,
            usuarios.nombre_completo,
            usuarios.correo,
            usuarios.telefono,
            usuarios.usuario,
            usuarios.id_rol,
            roles.rol
        FROM usuarios
        INNER JOIN roles
            ON usuarios.id_rol = roles.id_rol
        ORDER BY usuarios.id
    """)

    usuarios_db = cursor.fetchall()

    # =====================================================
    # OBTENER ROLES
    # =====================================================

    cursor.execute("""
        SELECT
            id_rol,
            rol
        FROM roles
        ORDER BY id_rol
    """)

    roles_db = cursor.fetchall()

    # =====================================================
    # USUARIO A EDITAR
    # =====================================================

    id_editar = request.args.get("editar")
    usuario_editar = None

    if id_editar:

        cursor.execute("""
            SELECT
                usuarios.id,
                usuarios.nombre_completo,
                usuarios.correo,
                usuarios.telefono,
                usuarios.usuario,
                usuarios.id_rol,
                roles.rol
            FROM usuarios
            INNER JOIN roles
                ON usuarios.id_rol = roles.id_rol
            WHERE usuarios.id = %s
        """, (id_editar,))

        usuario_editar = cursor.fetchone()

    cursor.close()

    # =====================================================
    # MOSTRAR PÁGINA
    # =====================================================

    return render_template(
        "gestionar_usuarios.html",
        usuarios=usuarios_db,
        roles=roles_db,
        usuario_editar=usuario_editar
    )


# =========================================================
# CREAR USUARIO
# =========================================================

@app.route(
    "/administrador/usuarios/crear",
    methods=["GET", "POST"]
)
def crear_usuario():

    # Verificar sesión
    if "id_usuario" not in session:
        return redirect(url_for("login"))

    # Solo administrador
    if session.get("rol") != "Administrador":
        return redirect(url_for("inicio_usuario"))

    # Crear usuario
    if request.method == "POST":

        nombre = request.form["nombre"]
        correo = request.form["correo"]
        telefono = request.form["telefono"]
        usuario = request.form["usuario"]
        password = request.form["password"]
        id_rol = request.form["id_rol"]

        password_hash = generate_password_hash(password)

        cursor = mysql.connection.cursor()

        # Comprobar usuario
        cursor.execute(
            "SELECT id FROM usuarios WHERE usuario = %s",
            (usuario,)
        )

        if cursor.fetchone():

            cursor.close()

            return """
            <script>
                alert("El nombre de usuario ya existe");
                window.location.href="/administrador/usuarios/crear";
            </script>
            """

        # Comprobar correo
        cursor.execute(
            "SELECT id FROM usuarios WHERE correo = %s",
            (correo,)
        )

        if cursor.fetchone():

            cursor.close()

            return """
            <script>
                alert("El correo electrónico ya está registrado");
                window.location.href="/administrador/usuarios/crear";
            </script>
            """

        # Insertar usuario
        cursor.execute("""
            INSERT INTO usuarios
            (
                nombre_completo,
                correo,
                telefono,
                usuario,
                contrasena,
                id_rol
            )
            VALUES (%s, %s, %s, %s, %s, %s)
        """, (
            nombre,
            correo,
            telefono,
            usuario,
            password_hash,
            id_rol
        ))

        mysql.connection.commit()
        cursor.close()

        return redirect(url_for("gestionar_usuarios"))

    # Obtener roles
    cursor = mysql.connection.cursor()

    cursor.execute("""
        SELECT
            id_rol,
            rol
        FROM roles
        ORDER BY id_rol
    """)

    roles_db = cursor.fetchall()

    cursor.close()

    return render_template(
        "crear_usuario.html",
        roles=roles_db
    )

@app.route("/administrador/usuarios/eliminar/<int:id_usuario>")
def eliminar_usuario(id_usuario):

    # Verificar sesión
    if "id_usuario" not in session:
        return redirect(url_for("login"))

    # Solo administrador
    if session.get("rol") != "Administrador":
        return redirect(url_for("inicio_usuario"))

    # No permitir eliminarse a sí mismo
    if id_usuario == session["id_usuario"]:

        return """
        <script>
            alert("No puedes eliminar tu propio usuario administrador");
            window.location.href="/administrador/usuarios";
        </script>
        """

    cursor = mysql.connection.cursor()

    cursor.execute(
        "DELETE FROM usuarios WHERE id = %s",
        (id_usuario,)
    )

    mysql.connection.commit()
    cursor.close()

    return redirect(url_for("gestionar_usuarios"))

@app.route("/usuarios")
def usuarios():

    cursor = mysql.connection.cursor()

    cursor.execute("""
        SELECT
            usuarios.id,
            usuarios.nombre_completo,
            usuarios.correo,
            usuarios.telefono,
            usuarios.usuario,
            usuarios.id_rol,
            roles.rol
        FROM usuarios
        INNER JOIN roles
            ON usuarios.id_rol = roles.id_rol
        ORDER BY usuarios.id
    """)

    datos = cursor.fetchall()

    cursor.close()

    return {
        "mensaje": "Conexión exitosa",
        "cantidad": len(datos),
        "usuarios": datos
    }

# =========================================================
# REPORTE DE USUARIOS Y ROLES
# =========================================================

@app.route("/reporte")
def reporte():

    # Verificar que haya iniciado sesión
    if "id_usuario" not in session:
        return redirect(url_for("login"))

    # Solo administrador
    if session.get("rol") != "Administrador":
        return redirect(url_for("inicio_usuario"))

    # Obtener filtro
    rol_filtro = request.args.get("rol")

    cursor = mysql.connection.cursor()

    # =====================================================
    # CONSULTA MULTITABLA CON INNER JOIN
    # =====================================================

    if rol_filtro:

        cursor.execute("""
            SELECT
                usuarios.id,
                usuarios.nombre_completo,
                usuarios.correo,
                usuarios.telefono,
                usuarios.usuario,
                roles.rol
            FROM usuarios
            INNER JOIN roles
                ON usuarios.id_rol = roles.id_rol
            WHERE roles.rol = %s
            ORDER BY usuarios.id DESC
        """, (rol_filtro,))

    else:

        cursor.execute("""
            SELECT
                usuarios.id,
                usuarios.nombre_completo,
                usuarios.correo,
                usuarios.telefono,
                usuarios.usuario,
                roles.rol
            FROM usuarios
            INNER JOIN roles
                ON usuarios.id_rol = roles.id_rol
            ORDER BY usuarios.id DESC
        """)

    usuarios = cursor.fetchall()

    cursor.close()

    return render_template(
        "reporte.html",
        usuarios=usuarios,
        rol_filtro=rol_filtro
    )


# =========================================================
# EXPORTAR REPORTE A EXCEL
# =========================================================

@app.route("/reporte_excel")
def reporte_excel():

    # Verificar sesión
    if "id_usuario" not in session:
        return redirect(url_for("login"))

    # Solo administrador
    if session.get("rol") != "Administrador":
        return redirect(url_for("inicio_usuario"))

    # Obtener filtro
    rol_filtro = request.args.get("rol")

    cursor = mysql.connection.cursor()

    # =====================================================
    # CONSULTA MULTITABLA
    # =====================================================

    if rol_filtro:

        cursor.execute("""
            SELECT
                usuarios.id,
                usuarios.nombre_completo,
                usuarios.correo,
                usuarios.telefono,
                usuarios.usuario,
                roles.rol
            FROM usuarios
            INNER JOIN roles
                ON usuarios.id_rol = roles.id_rol
            WHERE roles.rol = %s
            ORDER BY usuarios.id DESC
        """, (rol_filtro,))

    else:

        cursor.execute("""
            SELECT
                usuarios.id,
                usuarios.nombre_completo,
                usuarios.correo,
                usuarios.telefono,
                usuarios.usuario,
                roles.rol
            FROM usuarios
            INNER JOIN roles
                ON usuarios.id_rol = roles.id_rol
            ORDER BY usuarios.id DESC
        """)

    datos = cursor.fetchall()

    cursor.close()

    # =====================================================
    # CREAR ARCHIVO EXCEL
    # =====================================================

    libro = Workbook()

    hoja = libro.active

    hoja.title = "Reporte Rentec"

    # Encabezados
    hoja.append([
        "ID",
        "Nombre completo",
        "Correo",
        "Teléfono",
        "Usuario",
        "Rol"
    ])

    # Datos
    for fila in datos:

        hoja.append([
            fila[0],
            fila[1],
            fila[2],
            fila[3],
            fila[4],
            fila[5]
        ])

    # =====================================================
    # GUARDAR EN MEMORIA
    # =====================================================

    archivo = io.BytesIO()

    libro.save(archivo)

    archivo.seek(0)

    # Descargar Excel
    return send_file(
        archivo,
        download_name="reporte_rentec.xlsx",
        as_attachment=True
    )
@app.route("/agregar_al_carrito", methods=["POST"])
def agregar_al_carrito():
    productos_carrito = session.get("carrito", [])
    accion = request.form.get("accion")

    if accion == "agregar":
        nombre = request.form.get("nombre", "").strip()

        try:
            precio_hora = max(0, int(request.form.get("precio_hora", 0)))
            precio_dia = max(0, int(request.form.get("precio_dia", 0)))
            tiempo = max(1, min(365, int(request.form.get("tiempo", 1))))
            cantidad = max(1, min(99, int(request.form.get("cantidad", 1))))
        except (ValueError, TypeError):
            return "Los datos del producto no son válidos.", 400

        duracion = request.form.get("duracion", "hora")

        if nombre and precio_hora > 0 and precio_dia > 0:
            productos_carrito.append({
                "nombre": nombre,
                "precio_hora": precio_hora,
                "precio_dia": precio_dia,
                "duracion": "dia" if duracion == "dia" else "hora",
                "tiempo": tiempo,
                "cantidad": cantidad
            })

            session["carrito"] = productos_carrito
            session.modified = True

    elif accion == "vaciar":
        session["carrito"] = []

    return redirect(url_for("carrito"))


@app.route("/actualizar_carrito/<int:id_producto>", methods=["POST"])
def actualizar_carrito(id_producto):
    productos = session.get("carrito", [])

    if 0 <= id_producto < len(productos):
        try:
            tiempo = int(request.form.get("tiempo", 1))
            cantidad = int(request.form.get("cantidad", 1))
        except (ValueError, TypeError):
            return "La duración y la cantidad deben ser números válidos.", 400

        if not (1 <= tiempo <= 365 and 1 <= cantidad <= 99):
            return "La duración o la cantidad están fuera del límite permitido.", 400

        duracion = request.form.get("duracion", "hora")

        productos[id_producto]["duracion"] = (
            "dia" if duracion == "dia" else "hora"
        )
        productos[id_producto]["tiempo"] = tiempo
        productos[id_producto]["cantidad"] = cantidad

        session["carrito"] = productos
        session.modified = True

    return redirect(url_for("carrito"))


@app.route("/eliminar_del_carrito/<int:id_producto>", methods=["POST"])
def eliminar_del_carrito(id_producto):
    productos = session.get("carrito", [])

    if 0 <= id_producto < len(productos):
        productos.pop(id_producto)
        session["carrito"] = productos
        session.modified = True

    return redirect(url_for("carrito"))


@app.route("/vaciar_carrito", methods=["POST"])
def vaciar_carrito():
    session["carrito"] = []
    session.modified = True

    return redirect(url_for("carrito"))


@app.route("/solicitar_alquiler", methods=["POST"])
def solicitar_alquiler():
    productos = session.get("carrito", [])

    if not productos:
        return redirect(url_for("carrito"))

    return render_template(
        "solicitud_alquiler.html",
        carrito=productos
    )


@app.route("/generar_factura", methods=["POST"])
def generar_factura():
    cliente = {
        "nombre": request.form.get("nombre", "").strip(),
        "apellido": request.form.get("apellido", "").strip(),
        "telefono": request.form.get("telefono", "").strip(),
        "direccion": request.form.get("direccion", "").strip(),
        "tipo_documento": request.form.get("tipo_documento", "").strip(),
        "numero_documento": request.form.get("numero_documento", "").strip(),
        "metodo_pago": request.form.get("metodo_pago", "").strip()
    }

    if not all(cliente.values()):
        return "Completa todos los datos del formulario.", 400

    productos = session.get("carrito", [])

    if not productos:
        return redirect(url_for("carrito"))

    total = 0
    productos_factura = []

    for producto in productos:
        duracion = producto.get("duracion", "hora")
        tiempo = int(producto.get("tiempo", 1))
        cantidad = int(producto.get("cantidad", 1))

        precio = int(
            producto["precio_dia"]
            if duracion == "dia"
            else producto["precio_hora"]
        )

        subtotal = precio * tiempo * cantidad
        total += subtotal

        productos_factura.append({
            "nombre": producto["nombre"],
            "duracion": duracion,
            "tiempo": tiempo,
            "cantidad": cantidad,
            "precio": precio,
            "subtotal": subtotal
        })

    return render_template(
        "factura_alquiler.html",
        cliente=cliente,
        productos=productos_factura,
        total=total
    )


@app.route("/logout")
def logout():

    session.clear()

    return redirect(url_for("inicio"))

if __name__ == "__main__":

    print("======================================")
    print("       RENTEC - FLASK INICIADO")
    print("======================================")
    print("Servidor: http://127.0.0.1:5000")
    print("======================================")

    app.run(debug=True)

from flask import render_template, request, redirect, url_for, session




