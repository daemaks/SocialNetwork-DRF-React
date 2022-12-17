import { useThreads } from "../hooks/threadsLoader"
import Loader from "../components/loader"

export default function TreadsList() {

    const {loading, threads} = useThreads()

    return (
        <div>
        { loading && <Loader /> }
        { threads.map(thread => <thread thread={ thread } key={ thread.id } />)}
        </div>
    )
}