import { useThreads, useCommunityThreads } from "../hooks/threadsLoader"
import { Thread } from "../components/thread"
import Loader from "../components/loader"


export default function TreadsList() {

    const {loading, threads} = useThreads()
    console.log(threads)
    return (
            <div className="flex max-w-full mt-12 ml-80">
                <div className="flex w-full pt-8">
                    <div className="w-3/5">
                        { loading && <Loader /> }
                        { threads.map(thread => <Thread thread={ thread } key={ thread.id } />)}
                    </div>
                    <div className="w-2/5 h-full">
                    </div>
                </div>
            </div>
    )
}
