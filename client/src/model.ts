export interface IThread {
    id: number
    username: string
    community: string
    title: string
    content?: string
    image?: string
    create_at: string
    update_at: string
}

export interface ICommunity {
    id: number
    tag: string
    title: string
    description?: string
    image?: string
    members: number[]
}