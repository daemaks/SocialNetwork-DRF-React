import { IThread } from "../model"
export default function getTime( thread: IThread | null ) {
    if (thread) {
        const dateNow = new Date()
        const dateThread = new Date(thread.updated_at)
        const timeDifference  = (dateNow.getTime() - dateThread.getTime())
        const hourDifference = timeDifference / (1000 * 3600)
        if (hourDifference > 23) {
            const dayDifference = timeDifference / (1000 * 3600 * 24)
            return `${Math.round(dayDifference)} days`
        } else {
            return `${Math.round(hourDifference)} hours`
        }
    }
}