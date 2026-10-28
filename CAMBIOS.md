# Cambios del proyecto Subnáutica

Resumen de lo que se quitó y se agregó, con el código de **antes** y **después**.

---

## 1. Se eliminó "Fuentes"

### 1.1 Menú de `index.html`

**Antes**

```html
<a href="#exploracion">
    Exploración
</a>

<a href="#fuentes">
    Fuentes
</a>

<a href="usuarios.html">
    Usuarios
</a>
```

**Después**

```html
<a href="#exploracion">
    Exploración
</a>

<a href="usuarios.html">
    Usuarios
</a>
```

### 1.2 Menú de `usuarios.html`

**Antes**

```html
<a href="index.html#exploracion">Exploración</a>

<a href="index.html#fuentes">Fuentes</a>

<a href="usuarios.html">Usuarios</a>
```

**Después**

```html
<a href="index.html#exploracion">Exploración</a>

<a href="usuarios.html">Usuarios</a>
```

### 1.3 Sección completa en `index.html`

Se borró toda la **SECCIÓN 06 - FUENTES** (unas 170 líneas). Esta parte estaba entre la sección de Exploración y el `</main>`:

```html
<!-- SECCIÓN 06 - FUENTES -->
<section id="fuentes" class="seccion seccion-oscura">
    ...
    <h2>Investigación y conocimiento</h2>
    ...
    <div class="tarjetas">
        <article class="tarjeta fuente-tarjeta"> National Geographic ... </article>
        <article class="tarjeta fuente-tarjeta"> NOAA Ocean Explorer ... </article>
        <article class="tarjeta fuente-tarjeta"> Woods Hole ... </article>
        <article class="tarjeta fuente-tarjeta"> Smithsonian Ocean ... </article>
        <article class="tarjeta fuente-tarjeta"> NOAA Sanctuaries ... </article>
    </div>
    ...
</section>
```

> El CSS de estas clases **no se borró**, porque `tarjeta`, `texto-oscura`, `etiqueto`, etc. también se usan en otras secciones de la página.

---

## 2. Formulario de `usuarios.html`

### 2.1 HTML

**Antes:** dentro de la página había **otra página completa** pegada (`<!DOCTYPE>`, `<html>`, `<head>`, `<body>`), y eso es un error. Además, el apellido no se podía escribir (`readonly`) y el botón decía "clear".

```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Formulario</title>
</head>
<body>
    <form action="" method="">
        <table>
            ...
            <input type="text" placeholder="Apellido solo lectura" readonly name="lastname">
            ...
            <td colspan="2" align="center">
                <input type="submit" value="Enviar">
                <input type="reset" value="clear">
            </td>
        </table>
    </form>
</body>
</html>
```

**Después:** quedó solo el formulario, metido en una caja con su propia clase `caja-formulario`. El título usa las clases `numero` y `descripcion`, que ya existían.

```html
<div class="caja-formulario">

    <p class="numero">
        ESCRÍBENOS
    </p>

    <h2>
        Déjanos tu comentario
    </h2>

    <p class="descripcion">
        Cuéntanos qué te pareció nuestra expedición.
    </p>

    <form action="" method="">
        <table>
            ... (Nombre, Apellido, E-mail, Género, Comentario) ...
            <input type="text" placeholder="Coloque su apellido" name="lastname" id="lastname">
            ...
            <td colspan="2" class="botones">
                <input type="submit" value="Enviar">
                <input type="reset" value="Borrar">
            </td>
        </table>
    </form>

</div>
```

Cambios pequeños dentro del formulario:

| Campo | Antes | Después |
| --- | --- | --- |
| Nombre | `maxlength="10"` | `maxlength="30"` (los nombres largos no cabían) |
| Apellido | `readonly`, sin `id` | se puede escribir y tiene `id="lastname"` |
| Comentario | iba de 3.º y con `rows="10"` | va al final y con `rows="6"` |
| Botón borrar | `value="clear"` | `value="Borrar"` |
| Celda de botones | `align="center"` | `class="botones"` |

### 2.2 CSS

**Se quitó** esta regla, que centraba el formulario con flex:

```css
form {
    display: flex;
    justify-content: center;
    align-items: center;
    margin-top: 100px;
}
```

**Se reutilizó lo que ya existía:**

| Clase que ya existía | Qué le da al formulario |
| --- | --- |
| `.numero` | el texto verde pequeño "ESCRÍBENOS" |
| `.descripcion` | el texto gris de abajo del título |

**Se agregó** un bloque `FORMULARIO`, con los mismos colores que ya usa la página (`#062632`, `#031923`, `#0a4a59`, `#00a896`, `#00d6c3`):

| Regla nueva | Para qué sirve |
| --- | --- |
| `.caja-formulario` | la caja: ancho, fondo, borde, esquinas redondas y sombra |
| `.caja-formulario h2` | título más pequeño que los otros de la página |
| `.caja-formulario form`, `table`, `td`, `label` | espacios y color de las etiquetas |
| `input[type="text"]`, `input[type="email"]`, `textarea` | campos oscuros con bordes redondeados |
| `input:focus`, `textarea:focus` | el borde se pone verde agua al hacer clic |
| `input[type="radio"]` | radio buttons de color verde agua |
| `.botones` y `.botones input` | botones redondos como el botón "Inicio" del menú |
| `.botones input[type="submit"]` / `[type="reset"]` | "Enviar" relleno y "Borrar" solo con borde |
| `.botones input:hover` | cambio de color al pasar el mouse |

Ejemplo de cómo se ven las reglas (siguen el mismo formato del resto del archivo):

```css
/* =========================
   FORMULARIO
========================= */

.caja-formulario {
    max-width: 650px;

    margin: 90px auto 0;

    padding: 45px 40px;

    background: #062632;

    border: 1px solid #0a4a59;

    border-radius: 18px;

    box-shadow: 0 20px 50px rgba(0, 0, 0, 0.4);
}

.botones input {
    padding: 12px 35px;

    margin: 0 8px;

    border: 1px solid #00a896;

    border-radius: 25px;

    font-size: 14px;

    cursor: pointer;

    transition: 0.3s;
}
```

También se agregó esto en el `@media (max-width: 600px)` que ya existía, para que en el celular las filas queden una debajo de otra:

```css
.caja-formulario {
    padding: 30px 20px;
}

.caja-formulario td {
    display: block;
}
```

---

## 3. Lo que no se tocó

- `formulario.html` (es el ejercicio de práctica).
- `estilos.css` y `media tecnica subnáutica.css`.
- El enlace "El océano desconocido" de `usuarios.html` apunta a `oceano.html`, que **no existe**. Queda pendiente decidir si se cambia a `index.html#oceano`.
