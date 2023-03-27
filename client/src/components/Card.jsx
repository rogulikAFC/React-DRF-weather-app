export default function Card({elName, modName, title, children}) {
    return (
        <div className={`card ${elName} ${modName}`}>
            <h2 className="card__title"> {title} </h2>
            <hr />

            <div className="card__content">
                {children}
            </div>
        </div>
    )
}