import bpy
import math

def crear_material(nombre, color_rgb):
    mat = bpy.data.materials.new(name=nombre)
    mat.diffuse_color = (*color_rgb, 1.0)
    return mat

def generar_escenario():
    
    bpy.ops.object.select_all(action='SELECT')
    bpy.ops.object.delete()

    mat_pared_a = crear_material("ParedOscura", (0.1, 0.1, 0.1))
    mat_pared_b = crear_material("ParedDetalle", (0.8, 0.2, 0.0))
    mat_suelo = crear_material("Suelo", (0.2, 0.2, 0.2))

    largo_pasillo = 40
    ancho_pasillo = 4

    # 4. Construcción curva
    for i in range(largo_pasillo):

        curva = math.sin(i * 0.3) * 4

        # Pared Izquierda
        bpy.ops.mesh.primitive_cube_add(
            location=(-ancho_pasillo + curva, i * 2, 1)
        )
        pared_izq = bpy.context.active_object

        if i % 2 == 0:
            pared_izq.data.materials.append(mat_pared_a)
        else:
            pared_izq.data.materials.append(mat_pared_b)

        pared_izq.scale.z = 1.5

        # Pared Derecha
        bpy.ops.mesh.primitive_cube_add(
            location=(ancho_pasillo + curva, i * 2, 1)
        )
        pared_der = bpy.context.active_object
        pared_der.data.materials.append(mat_pared_a)
        pared_der.scale.z = 1.5

        # Suelo
        bpy.ops.mesh.primitive_plane_add(
            size=2,
            location=(curva, i * 2, 0)
        )
        suelo = bpy.context.active_object
        suelo.scale.x = ancho_pasillo
        suelo.scale.y = 1
        suelo.data.materials.append(mat_suelo)



    bpy.ops.object.camera_add(location=(0, 0, 3))
    camara = bpy.context.active_object
    bpy.context.scene.camera = camara

    frames_totales = 150

    for frame in range(frames_totales):

        bpy.context.scene.frame_set(frame)

        y_pos = frame * 0.4
        x_pos = math.sin((y_pos / 2) * 0.3) * 4

        camara.location = (x_pos, y_pos, 3)
        camara.rotation_euler[0] = math.radians(75)

        camara.keyframe_insert(data_path="location")
        camara.keyframe_insert(data_path="rotation_euler")

    bpy.context.scene.frame_end = frames_totales

# Ejecutar
generar_escenario()