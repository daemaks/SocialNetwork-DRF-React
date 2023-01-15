import { useParams } from 'react-router-dom'
import { useUser } from '../hooks/userLoader'
import { useUserThreads } from '../hooks/threadsLoader'
import Loader from "../components/loader"
import { Thread } from "../components/thread"

export default function UserPage() {

    const { slug } = useParams()
    const { user } = useUser(slug)
    const {loading, threads} = useUserThreads(slug)


    const getBackground = (data:any) => {
        if (data != null) {
            return `url(${data})`
        } else {
            return 'url(http://getwallpapers.com/wallpaper/full/a/b/e/667524.jpg)'
        }
    }

    return(
        <div className="flex max-w-full mt-12 ml-60">
            <div className="flex flex-row justify-center mx-auto py-5 px-6">
                <div className="w-[640px]">
                    { loading && <Loader /> }
                    { threads.map(thread => <Thread thread={ thread } key={ thread.id } />)}
                </div>
                <div className='bg-white border border-gray-300 rounded block w-[320px] ml-6'>
                    <div className='rounded-t h-20 bg-cover w-full' style={{ backgroundImage: getBackground(user?.bg_image) }}></div>
                    <div className='w-full p-2'>
                        <div className='flex content-center mx-auto h-16 w-16 overflow-hidden rounded-full border-2 bg-white'>
                            <img src={user?.avatar}/>
                        </div>
                        <div className='text-lg pt-2 text-center capitalize font-semibold'>
                            <h1>{user?.username}</h1>
                        </div>
                        <div className='text-center text-sm text-gray-400 font-medium pb-2'>
                            <span>u/{user?.username}</span>
                        </div>
                        <hr />
                        <div className='pt-2 leading-5 text-sm'>
                            <p>{user?.about}</p>
                        </div>
                    </div>
                </div>
            </div>
        </div>
    )
}