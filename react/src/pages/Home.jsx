import { useEffect } from "react";
import { api } from "../lib/api";

async function getBooks() {
    const res = await api.get('/books')
    return res
}

export default function Home() {
    useEffect(() => {
        const getData = async (req, res) => {
            const data = await getBooks()
            console.log(data)
        }

        getData()
    }, [])
  return (
    <>
      <header className="text-2xl font-semibold py-4 text-center bg-white">
        Catálogo de Livros
      </header>

      <main>

      </main>
    </>
  );
}
