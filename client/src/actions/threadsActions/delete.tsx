
import axiosInstance from "../../axios"

export default function DeleteThread (id : number) {

    axiosInstance
        .delete(`threads/thread/${id}/`)
        .then(() => {
            window.location.reload()
        })

    return 
}