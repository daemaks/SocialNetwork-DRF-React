import { useThreads } from "../hooks/threadsLoader"
import Loader from "../components/loader"
import { Thread } from "../components/thread"

export default function TreadsList() {

    const {loading, threads} = useThreads()

    return (
        <div>
        { loading && <Loader /> }
        { threads.map(thread => <Thread thread={ thread } key={ thread.id } />)}
        </div>
    )
}