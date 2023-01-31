import { IComment, IThread } from "../model"
export default function getTime( obj: IThread | IComment | null ) {
    if (obj) {
        const dateNow = new Date()
        const dateThread = new Date(obj.created_at)
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