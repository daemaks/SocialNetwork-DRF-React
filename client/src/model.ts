export interface ICommunity {
    id: number;
    tag: string;
    title: string;
    slug: string;
    description: string;
    image?: string;
    bg_image?: string;
    created_at: Date;
    members: any[];
}

export interface IThread {
    id: number
    username: string
    community: ICommunity
    title: string
    content?: string
    image?: string
    created_at: Date
    updated_at: Date
}

export interface ITag {
    id: number
    title: string
}

export interface IUser {
    id: number;
    username: string;
    slug: string;
    avatar?: string;
    bg_image?: string;
    about: string;
    date_joined: Date;
    is_staff: boolean;
}

export interface IComment {
    id: number;
    username: IUser;
    thread: number;
    text: string;
    created_at: Date;
    updated_at: Date;
}