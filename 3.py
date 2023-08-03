public class Customer
{
    [Column("UserId")]
    public int CustomerId { get; set; }

    // ...
}


// то же самое с помощью Fluent API

protected override void OnModelCreating(DbModelBuilder modelBuilder)
{
     modelBuilder.Entity<Customer>().Property(c => c.CustomerId)
         .HasColumnName("UserId");
}