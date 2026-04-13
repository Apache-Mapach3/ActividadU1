const readline = require('readline').createInterface({ input: process.stdin, output: process.stdout });
const prompt = q => new Promise(r => readline.question(q, r));

async function main() {
    // crear matriz inicializada en null//
    let sala = Array.from({ length: 3 }, () => Array(4).fill(null));
    let opcion = 0;

    while (opcion !== 4) {
        // mostrar menu principal//
        console.log("\n1. Ver sala\n2. Ocupar\n3. Liberar\n4. Salir");
        opcion = parseInt(await prompt("Opcion: "));

        if (opcion === 1) {
            // recorrer e imprimir sala//
            for (let i = 0; i < 3; i++) {
                let fila = "";
                for (let j = 0; j < 4; j++) {
                    fila += `[${i + 1},${j + 1}:${sala[i][j] || "LIBRE"}]\t`;
                }
                console.log(fila);
            }
        } else if (opcion === 2 || opcion === 3) {
            // leer coordenadas unificadas//
            let f = parseInt(await prompt("Fila: ")) - 1;
            let c = parseInt(await prompt("Columna: ")) - 1;

            // validar limites exactos//
            if (f >= 0 && f < 3 && c >= 0 && c < 4) {
                if (opcion === 2) {
                    if (sala[f][c]) console.log("Ocupado por " + sala[f][c]);
                    else sala[f][c] = await prompt("Nombre: ");
                } else {
                    if (!sala[f][c]) console.log("Ya estaba libre");
                    else sala[f][c] = null;
                }
            } else console.log("Invalido");
        }
    }
    // salir del sistema//
    readline.close();
}
main();