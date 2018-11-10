import subprocess

subprocess(["hmmscan",
                 "-o",
                 "./resultados/salida.hmm",
                 "./database/minifam",
                 "./resultados/resultados.fa"
                 ]
        )